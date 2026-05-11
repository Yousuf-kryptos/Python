import sqlite3

#### DATABASE ####
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY,
               name TEXT,
               age INTEGER,
               course TEXT,
               year INTEGER
               )''')

conn.commit()

#### DATABASE FUNCTIONS ####

def table_info():
    cursor.execute("PRAGMA table_info(students)")
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def add_students():
    s_id = input("Enter Student ID: ")
    s_name = input("Enter Student Name: ")
    s_age = input("Enter Age: ")
    course = input("Enter Course Name(Like CSE,ECE,etc..): ")
    year = input("Enter Batch Year: ")

    if s_id == "" or s_name == "" or s_age == "" or course == "" or year == "":
        print("All Fields are required")
        return

    # Check Duplicates
    cursor.execute("SELECT id FROM students WHERE id=?",(s_id,))

    row = cursor.fetchone()

    if row:
        print("Student ID already exists")
        return

    try:
        cursor.execute("INSERT INTO students VALUES (?,?,?,?,?)",
                   (s_id,s_name,s_age,course,year))
        conn.commit()
        print("Student Added Successfully")

    except sqlite3.Error as error:
        print("Error Occurred: ",error)

def view_students():
    cursor.execute("SELECT * FROM students")

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No Students found\n")
        return
    
    print("-"*20,"Students Records","-"*20)

    for row in rows:
        print(f"Student ID: {row[0]}")
        print(f"Student Name: {row[1]}")
        print(f"Student Age: {row[2]}")
        print(f"Course Name: {row[3]}")
        print(f"Batch Year: {row[4]}")
        print("-"*40)

def search_students():
    s_id = input("Enter Student ID to search: ")

    cursor.execute("SELECT * FROM students WHERE id=?",(s_id,))

    rows = cursor.fetchone()

    if rows:
        print("Student Found\n")
        print("-"*40)
        print(f"Student ID: {rows[0]}")
        print(f"Student Name: {rows[1]}")
        print(f"Student Age: {rows[2]}")
        print(f"Course Name: {rows[3]}")
        print(f"Batch Year: {rows[4]}")
        print("-"*40)
    
    else:
        print("No Student Found")

def update_students():
    s_id = input("Enter student id to be updated: ")

    cursor.execute("SELECT * FROM students WHERE id=?",(s_id,))

    rows = cursor.fetchone()

    if not rows:
        print("No Student Found\n")
        return
    
    print("Leave empty if no changes\n")

    name = input("Enter the name to be updated: ")
    age = input("Enter the age to be updated: ")
    course = input("Enter the course to be updated: ")
    year = input("Enter the year to be updated: ")

    if name == "":
        name = rows[1]

    if age == "":
        age = rows[2]

    if course == "":
        course = rows[3]
    
    if year == "":
        year = rows[4]

    cursor.execute("UPDATE students SET name=?,age=?,course=?,year=? WHERE id=?",(name,age,course,year,s_id))

    conn.commit()
    print("Student Database updated successfully")

def delete_students():
    s_id = input("Enter Student ID to be deleted: ")

    cursor.execute("SELECT * FROM students WHERE id=?",(s_id,))

    rows = cursor.fetchone()

    if not rows:
        print("No Student Found\n")
        return
    
    cursor.execute("DELETE FROM students WHERE id=?",(s_id,))
    conn.commit()

    print("Student Deleted From Database\n")

while True:
    print("------- Student Management System -------")
    print("0. Table info")
    print("1. Add Students")
    print("2. View Students")
    print("3. Search Students")
    print("4. Update Students Data")
    print("5. Delete Students Data")
    print("6. Exit")
    
    choice = int(input("Enter your Choice: "))

    if choice == 0:
        table_info()
        
    elif choice == 1:
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

## DATABASE CLOSING ##
cursor.close()
conn.close()
