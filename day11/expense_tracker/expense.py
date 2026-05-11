import sqlite3

conn = sqlite3.connect('expense.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS expense(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               amount INTEGER,
               category TEXT,
               date TEXT
               ) ''')

conn.commit()

def add_expense():
    Id = input("Enter Product ID: ")

    cursor.execute("SELECT * FROM expense WHERE id=?",(Id,))

    row = cursor.fetchone()

    if row:
        print("Product ID already exists")
        return
    
    Name = input("Enter Product Name: ")
    Amount = input("Enter the Product Amount: ")
    Category = input("Enter the Product Category: ")
    Date = input("Enter the Date(YYYY-MM-DD): ")

    cursor.execute("INSERT INTO expense VALUES(?,?,?,?,?)",(Id,Name,Amount,Category,Date))
    conn.commit()
    print("\nAdded Successfully!\n")

def view_products():
    cursor.execute("SELECT * FROM expense")

    rows = cursor.fetchall()

    if(len(rows) == 0):
        print("No Data Found")
        return
    
    for row in rows:
        print("-"*15,"Product Details","-"*15)
        print(f"Product ID: {row[0]}")
        print(f"Product Name: {row[1]}")
        print(f"Product Amount: Rs.{row[2]}")
        print(f"Category: {row[3]}")
        print(f"Date: {row[4]}\n")

def search_by_category():
    category = input("Enter the category to search: ")

    cursor.execute("SELECT * FROM expense WHERE category=?",(category,))
    rows = cursor.fetchall()

    if not rows:
        print("No Category Found")
        return
    
    print(f"\n ------ {category.upper()} Expenses ------\n")
    
    for row in rows:
        print(f"Product ID: {row[0]}")
        print(f"Product Name: {row[1]}")
        print(f"Product Amount: Rs.{row[2]}")
        print(f"Category: {row[3]}")
        print(f"Date: {row[4]}")

        print("-"*30)

def total_expenses():
    cursor.execute("SELECT SUM(amount) FROM expense")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print(f"Total Expenses : Rs.{total}\n")

def update_products():
    Id = input("Enter Product ID to update: ")

    cursor.execute("SELECT * FROM expense WHERE id=?",(Id,))
    row = cursor.fetchone()

    if not row:
        print("Product ID not Found!")
        return
    
    print("Leave Blank If no changes\n")

    Name = input("Enter Product Name to update: ")
    Amount = input("Enter Product Amount to update: ")
    Category = input("Enter Category to update: ")
    Date = input("Enter Date to update: ")

    if Name == "":
        Name = row[1]

    if Amount == "":
        Amount = row[2]
    
    if Category == "":
        Category = row[3]
    
    if Date == "":
        Date = row[4]

    cursor.execute("UPDATE expense SET name=?, amount=?, category=?,date=? WHERE id=?",
                   (Name,Amount,Category,Date,Id))
    
    conn.commit()
    print("Updated Successfully!")

def category_report():
    cursor.execute("SELECT category,SUM(amount) FROM expense GROUP BY category")

    rows = cursor.fetchall()

    if not rows:
        print("No data Found\n")
        return
    
    for row in rows:
        print(f"Category: {row[0]}")
        print(f"Total: Rs.{row[1]}")

        print("-"*30)

def monthly_report():
    month = input("Enter the month(YYYY-MM): ")
    cursor.execute("SELECT * FROM expense WHERE date LIKE ?",(month+"%",))

    rows = cursor.fetchall()

    if not rows:
        print("No Date Found")
        return
    
    total = 0
    print(f"------ {month} Report -----\n")
    for row in rows:
        print(f"Product ID: {row[0]}")
        print(f"Product Name: {row[1]}")
        print(f"Product Amount: RS.{row[2]}")
        print(f"Category: {row[3]}")
        print(f"Date: {row[4]}\n")
        print("-"*30)

        total += row[2]

    print(f"Monthly Expenses: {total}\n")

def delete_expenses():
    Id = input("Enter the Product ID to be deleted: ")

    cursor.execute("SELECT * FROM expense WHERE id=?",(Id,))

    row = cursor.fetchone()

    if not row:
        print("Product ID not found\n")
        return
    
    cursor.execute("DELETE FROM expense WHERE id=?",(Id,))
    conn.commit()
    print("Product Deleted Successfully\n")

while True:
    print("===== MainMenu =====")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Search By Category")
    print("4. Total Expenses")
    print("5. Update Products Details")
    print("6. Category Report")
    print("7. Monthly Report")
    print("8. Delete Expenses")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_products()

    elif choice == 3:
        search_by_category()

    elif choice == 4:
        total_expenses()
    
    elif choice == 5:
        update_products()
    
    elif choice == 6:
        category_report()
    
    elif choice == 7:
        monthly_report()
    
    elif choice == 8:
        delete_expenses()

    elif choice == 9:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")

cursor.close()
conn.close()