from library_project_module import *

print("""
WELCOME TO LIBRARY!

1. SHOW THE BOOKS
2. SEARCH FOR A BOOK
3. ADD A BOOK 
4. DELETE A BOOK 
5. UPDATE THE EDITION OF A BOOK

(ENTER "q" TO EXIT.)

""")

library=Library()

while True:
    operation=input("Choose an operation(1,2,3,4,5):")
    if operation=="q":
        print("THANKS FOR VISITING OUR LIBRARY!")
        library.disconnection()
        break

    elif operation=="1":
        library.show_books()

    elif operation=="2":
        name=input("Which book are you searching for?(Enter the name.):")
        print("Searching for the book...")
        time.sleep(2)
        library.search_book(name)

    elif operation=="3":
        name=input("Enter the book name:")
        author=input("Enter the author:")
        publisher=input("Enter the publisher:")
        genre=input("Enter the genre:")
        edition=input("Enter the edition:")
        new_book=Book(name,author,publisher,genre,int(edition))
        print("Adding the book...")
        time.sleep(2)
        library.append_book(new_book)
        print("The book is successfully added.")

    elif operation=="4":
        name=input("Enter the name of the book you want to delete:")
        answer=input("Are you sure?(Enter 'y' or 'n'):")
        if answer=="y":
            print("Deleting the book...")
            library.delete_book(name)
            print("The book is successfully deleted.")


    elif operation=="5":
        name=input("Enter the name of the book you want to update:")
        print("Updating the book...")
        a=library.update_edition(name)
        if a==1:
            print("The book edition is successfully updated.")
    else:
        print("INVALID OPERATION")
