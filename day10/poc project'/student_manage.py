# Student Management System

# Build - 1
# Basic Needs for this Project is to get information like id,name,age,course,year and 
# get information dictionary format and store this data using list so it can be easy to access 
# using  keys and get values and store it in list to do some operations like append and remove

# Build - 2
# In this, I updated the code by using json, file handling,try...except and updating the details
# First, I give file name and it tries to open and load the file using read mode in try block,
# if the file doesn’t exists it goes except block where I give empty students list to add the details.
# Then I define the save_data() method to save the data in the list to file.
# For that, I update the file by opening the file in write mode and I dump the data using json.dump(list_name,file_name,indent).
# (Important Note: dump() -> writes to file, dumps() -> convert python to JSONstring).
# After that, I define the update_students() method to update the details.
# So After one cycle of entering the data, whenever I run this code it will automatically load the data from JSON.

import json

file_name = "students.json"

try:
    with open (file_name,"r") as file:
        students = json.load(file)

except:
    students = []

def save_data():
    with open (file_name,'w') as file:
        json.dump(students,file,indent = 4)

def add_students():
    s_id = input("Enter Student ID: ")
    
    for student in students:
        if student['Id'] == s_id:
            print("Student Id already exists")
            return
    s_name = input("Enter Student Name: ")
    s_age = input("Enter Age: ")
    course = input("Enter Course Name(Like CSE,ECE,etc..): ")
    year = input("Enter Batch Year: ")

    student = {
        "Id" : s_id,
        "Name" : s_name,
        "Age" : s_age,
        "Course" : course,
        "Year" : year
    }

    students.append(student)
    save_data()
    print("Added Successfully\n")

def view_students():
    if len(students) == 0:
        print("No Students found\n")
    else:
        print("\nStudents Details")
        print("-" * 30)

        for student in students:
            print(f"Student ID : {student['Id']}")
            print(f"Student Name : {student['Name']}")
            print(f"Student Age : {student['Age']}")
            print(f"Student Course : {student['Course']}")
            print(f"Student Year : {student['Year']}")
            print("-" * 30)

def search_students():
    s_id = input("Enter Student Id to search: ")

    for student in students:
        if student['Id'] == s_id:
            print("\nStudent Found")
            print("-" * 30)
            print(f"Student ID : {student['Id']}")
            print(f"Student Name : {student['Name']}")
            print(f"Student Age : {student['Age']}")
            print(f"Student Course : {student['Course']}")
            print(f"Student Year : {student['Year']}")
            print("-" * 30)
            return
        
    print("No Student Found")

def delete_students():
    s_id = input("Enter Student Id to delete: ")

    for student in students:
        if student['Id'] == s_id:
            students.remove(student)
            save_data()
            print("\nStudent Removed Successfully")
            return
        
    print("No Student Found\n")

def update_students():
    s_id = input("Enter Student Id to update the details: ")
    
    for student in students:
        if student['Id'] == s_id:
            print("Leave Blank if no changes")

            name = input("Enter new Name: ")
            age = input("Enter new age: ")
            course = input("Enter new course: ")
            year = input("Enter new year: ")

            if name:
                student["Name"] = name

            if age:
                student["Age"] = age

            if course:
                student["Course"] = course

            if year:
                student["Year"] = year

            save_data()
            print("\nUpdated Successfully")
            return
        
    print("Student Not Found\n")

while True:
    print("------- Student Management System -------")
    print("1. Add Students")
    print("2. View Students")
    print("3. Search Students")
    print("4. Update Students Data")
    print("5. Delete Students Data")
    print("6. Exit")
    
    choice = int(input("Enter your Choice: "))

    if choice == 1:
        add_students()

    elif choice == 2:
        view_students()
    
    elif choice == 3:
        search_students()

    elif choice == 4:
        update_students()

    elif choice == 5:
        delete_students()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid Choice\n")

