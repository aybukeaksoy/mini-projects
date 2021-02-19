#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs
# Through this project, the insurance costs data provided in the csv file will be examined by using Python. The goal is to understand the dataset and the relation between the attributes in insurance.csv file. 

# In[ ]:


import csv


# The each attribute will be appended to their own lists and stored there to use for further analysise later on. 
# There are 7 attributes in the dataset:
# - Age of the patient
# - Sex of the patient(female,male)
# - BMI(Body Mass Index) of the patient
# - Number of children of the patient 
# - Smoking status of the patient(yes,no)
# - U.S Region of the patient(northeast,northwest,southeast,southwest)
# - Yearly medical insurance costs of the patient
# 

# The below function called organize_data receives the attribute name("age","sex","bmi","children","smoker","region","charges")as parameter and is created to append each attribute to different lists. 

# In[5]:


def organize_data(attribute):
    
    with open("insurance.csv",newline='') as insurance_csv:
        attribute_list=[]
        data=csv.DictReader(insurance_csv,delimiter=",")
        for row in data:
            attribute_list.append(row[attribute])
    
    return attribute_list
        
    


# Attribute lists can be seen by running the below cell.

# In[59]:


ages=organize_data("age")
sexes=organize_data("sex")
bmis=organize_data("bmi")
number_of_children=organize_data("children")
smoking_statuses=organize_data("smoker")
regions=organize_data("region")
insurance_charges=organize_data("charges")

#print(ages)
#print(sexes)
#print(number_of_children)
#print(smoking_statuses)
#print(regions)
#print(insurance_charges)


# Dataset can be examined in terms of:
# 
# - The average age of patients
# - The percentage of male and female patients
# - The region which majority of patients are from
# - The percentage of male and female smokers
# - The average number of children patients have
# - The average yearly medical insurance costs of patients
# - The relation between the ages and the medical insurance charges
# - The relation between the sex and the medical insurance charges
# - The relation between the bmi and the medical insurance charges
# - The relation between the smoking statuses and the medical insurance charges

# The function below, calculates the average age of all individuals,females and males.

# In[46]:


def calculate_average_age(ages,sexes):
    
    #converting the type of ages in ages list from string to integer
    for i in range(len(ages)):
        ages[i]=int(ages[i])
    
    #calculating the age average of all ind.
    total_average=sum(ages)/len(ages)
    
    female_count=0
    female_age_sum=0
    male_count=0
    male_age_sum=0
    
    #counting the number of females and males and adding their ages to
    #female_age_sum and male_age_sum
    for i in range(len(ages)):
        if sexes[i]=="male":
            male_count+=1
            male_age_sum+=int(ages[i])
        else:
            female_count+=1
            female_age_sum+=int(ages[i])
    
    #calculating the female and male age average
    female_average=female_age_sum/female_count
    male_average=male_age_sum/male_count
    age_dict={"overall average":total_average,"female average":female_average,"male average":male_average}
    return age_dict
    


# By running the below cell, the averages can be seen.

# In[47]:


print("The overall age average:",calculate_average_age(ages,sexes)["overall average"])
print("The female age average:",calculate_average_age(ages,sexes)["female average"])
print("The male age average:",calculate_average_age(ages,sexes)["male average"])
    


# The function below, calculates the number and percentage of female and male patients.

# In[48]:


def calculate_sex_percentage(sexes):
    
    total=len(sexes)
    female_count=sexes.count("female")
    male_count=sexes.count("male")
    
    female_perc=female_count/total*100
    male_perc=male_count/total*100
    sexes_dict={"female number":female_count,"male number":male_count,"female percentage":female_perc,"male percentage":male_perc}
    
    return sexes_dict


# By running the below cell, results can be seen.

# In[49]:


print("The number of female patients:",calculate_sex_percentage(sexes)["female number"])
print("The number of male patients:",calculate_sex_percentage(sexes)["male number"])
print("The percentage of female patients: %",calculate_sex_percentage(sexes)["female percentage"])
print("The percentage of male patients: %", calculate_sex_percentage(sexes)["male percentage"])


# The function below, finds the number of patients that live in each region of US and shows which region the majority of patients live in.   

# In[50]:


def calculate_region(regions):
    
    total=len(regions)
    region_list=["Northeast","Northwest","Southeast","Southwest"]
    northeast=regions.count("northeast")
    northwest=regions.count("northwest")
    southeast=regions.count("southeast")
    southwest=regions.count("southwest")
    region_list2=[northeast,northwest,southeast,southwest]
    
    #finding where majority comes from
    majority=region_list[region_list2.index(max(region_list2))]
    
    print("The number of patients living in:\nNortheast of US:{}\nNorthwest of US:{}\nSoutheast of US:{}\nSouthwest of US:{}".format(northeast,northwest,southeast,southwest))
    print("The majority is from:",majority)


# By running the below cell, the results can be seen.

# In[51]:


calculate_region(regions)


# The function below can be used to calculate the percentage of female and male smokers in all smokers. Also, the percentage of female smokers to all females and male smokers to all males can be calculated. 

# In[55]:


def calculate_smoker_percentage(smoking_statuses,sexes):
    
    female_smoker=0
    male_smoker=0
    
    for i in range(len(smoking_statuses)):
        if smoking_statuses[i]=="yes" and sexes[i]=="female":
            female_smoker+=1
        elif smoking_statuses[i]=="yes" and sexes[i]=="male":
            male_smoker+=1
    
    total_smoker=female_smoker+male_smoker
    f_perc=female_smoker/total_smoker*100
    m_perc=male_smoker/total_smoker*100
    
    #what percentage of females and males are smokers
    female_number=calculate_sex_percentage(sexes)["female number"]
    male_number=calculate_sex_percentage(sexes)["male number"]
    all_f_perc=female_smoker/female_number*100
    all_m_perc=male_smoker/male_number*100
    
    return [f_perc,m_perc,all_f_perc,all_m_perc]


# In[57]:


print("The %{} of all smokers are female.".format(calculate_smoker_percentage(smoking_statuses,sexes)[0]))
print("The %{} of all smokers are male.".format(calculate_smoker_percentage(smoking_statuses,sexes)[1]))
print("The %{} of females are smokers.".format(calculate_smoker_percentage(smoking_statuses,sexes)[2]))
print("The %{} of males are smokers.".format(calculate_smoker_percentage(smoking_statuses,sexes)[3]))


# From above results according to our data sampling, it can be observed that the percentage of male smokers are more than female smokers.

# The below function can be used to calculate both average number of children and yearly medical insurance costs of patients. 

# In[70]:


def calculate_avg(lst):
    
    l=len(lst)
    for i in range(l):
        lst[i]=float(lst[i])
    avg=sum(lst)/l
    
    return avg
    
    


# In[71]:


print("The average children number of patients are {}.".format(calculate_avg(number_of_children)))
print("The average yearly medical insurance cost of patients are {}.".format(calculate_avg(insurance_charges)))


# The relations between the attributes will be examined below:

# In[72]:


def relation_between(lst1,lst2,status):
    
    sum=0
    count=0
    for i in range(len(lst1)):
        if lst2[i]==status:
            sum+=float(lst1[i])
            count+=1
    return sum/count


# In[77]:


print("The average medical insurance cost of females are:",relation_between(insurance_charges,sexes,"female"))
print("The average medical insurance cost of males are:",relation_between(insurance_charges,sexes,"male"))
print("The average medical insurance cost of smokers are:",relation_between(insurance_charges,smoking_statuses,"yes"))
print("The average medical insurance cost of non-smokers are:",relation_between(insurance_charges,smoking_statuses,"no"))


# From results, it can be seen that the average medical insurance cost of smokers are about 3.8 times higher than non-smokers.

# In[95]:


def age_cost_relation(insurance_charges,ages):
    
    young_adults_count=0
    young_adults_sum=0
    adults_count=0
    adults_sum=0
    
    for i in range(len(ages)):
        
        if 18<=int(ages[i])<25:
            young_adults_count+=1
            young_adults_sum+=insurance_charges[i]
        else:
            adults_count+=1
            adults_sum+=insurance_charges[i]
            
    young_adults_avg=young_adults_sum/young_adults_count
    adults_avg=adults_sum/adults_count
    
    return young_adults_avg,adults_avg


# In[99]:


print("The average medical insurance cost for patients between 18-24 years old is:",age_cost_relation(insurance_charges,ages)[0])
print("The average medical insurance cost for patients between 25-64 years old is:",age_cost_relation(insurance_charges,ages)[1])


# The medical insurance cost for adults(25-64) is about 1.6 times higher than young-adults(18-24). 

# In[105]:


def bmi_cost_relation(bmis,insurance_charges):
    uw_count=0
    uw_sum=0
    n_count=0
    n_sum=0
    ow_count=0
    ow_sum=0
    o_count=0
    o_sum=0
    eo_count=0
    eo_sum=0
    for i in range(len(bmis)):
        if float(bmis[i])<18.5:
            uw_count+=1
            uw_sum+=insurance_charges[i]
        elif float(bmis[i])<25:
            n_count+=1
            n_sum+=insurance_charges[i]
        elif float(bmis[i])<30:
            ow_count+=1
            ow_sum+=insurance_charges[i]
        elif float(bmis[i])<35:
            o_count+=1
            o_sum+=insurance_charges[i]
        else:
            eo_count+=1
            eo_sum+=insurance_charges[i]
    return uw_sum/uw_count,n_sum/n_count,ow_sum/ow_count,o_sum/o_count,eo_sum/eo_count


# In[107]:


print("The average medical insurance cost for underweight patients is:",bmi_cost_relation(bmis,insurance_charges)[0])
print("The average medical insurance cost for normal weight patients is:",bmi_cost_relation(bmis,insurance_charges)[1])
print("The average medical insurance cost for overweight patients is:",bmi_cost_relation(bmis,insurance_charges)[2])
print("The average medical insurance cost for obese patients is:",bmi_cost_relation(bmis,insurance_charges)[3])
print("The average medical insurance cost for extremely obese patients is:",bmi_cost_relation(bmis,insurance_charges)[4])


# As seen from the results, while bmis are getting higher, the average medical insurance cost is getting higher too.

# In[ ]:




