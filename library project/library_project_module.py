import sqlite3
import time

class Book():
    def __init__(self,name,author,publisher,genre,edition):
        self.name=name
        self.author=author
        self.publisher=publisher
        self.genre=genre
        self.edition=edition

    def __str__(self):
        return "Book Name: {}\nAuthor: {}\nPublisher: {}\nGenre: {}\nEdition: {}\n".format(self.name,self.author,self.publisher,self.genre,self.edition)

class Library():
    def __init__(self):
        self.make_connection()

    def make_connection(self):
        self.connection=sqlite3.connect("library_project.db")
        self.cursor=self.connection.cursor()
        q="Create Table if not exists books(name TEXT,author TEXT,publisher TEXT,genre TEXT,edition INT)"
        self.cursor.execute(q)
        self.connection.commit()

    def disconnection(self):
        self.connection.close()

    def show_books(self):
        q="Select * From books"
        self.cursor.execute(q)
        books=self.cursor.fetchall()
        if len(books)==0:
            print("NO BOOKS IN LIBRARY")
        else:
            for b in books:
                book=Book(b[0],b[1],b[2],b[3],b[4])
                print(book)

    def search_book(self,name):
        q="Select * From books where name=?"
        self.cursor.execute(q,(name,))
        books=self.cursor.fetchall()
        if len(books)==0:
            print("THIS BOOK IS NOT IN LIBRARY")
        else:
            book=Book(books[0][0],books[0][1],books[0][2],books[0][3],books[0][4])
            print(book)

    def append_book(self,book):
        q="Insert into books Values(?,?,?,?,?)"
        self.cursor.execute(q,(book.name,book.author,book.publisher,book.genre,book.edition))
        self.connection.commit()

    def delete_book(self,name):
        q="Delete From books where name=?"
        self.cursor.execute(q,(name,))
        self.connection.commit()

    def update_edition(self,name):
        count=0
        q="Select * From books where name=?"
        self.cursor.execute(q,(name,))
        books=self.cursor.fetchall()
        for b in books:
            if b[0]==name:
                count+=1
        if count==0:
            print("THIS BOOK IS NOT IN LIBRARY")
            return 0
        else:
            edition=books[0][4]
            edition+=1
            q2="update books set edition=? where name=?"
            self.cursor.execute(q2,(edition,name))
            self.connection.commit()
            return 1
