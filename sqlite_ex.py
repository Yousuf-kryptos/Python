# # SQLite3 

# import sqlite3

# try:
#     conn = sqlite3.connect("sql.db")         # Make the connection to sqlite3 using connect()
#     cursor = conn.cursor()                   # Make the cursor object using cursor() to execute the queries
#     print("DB Init")

#     query = 'SELECT sqlite_version();'
#     cursor.execute(query)                    # Execute single SQL query

#     result = cursor.fetchall()               # Fetches all rows of query result set
#     print("SQLite Version is",format(result[0][0]))

#     cursor.close()                           # Closing the connection

# except sqlite3.Error as error:
#     print("Error Occured: ",error)

# finally:
#     if conn:
#         conn.close()
#         print("SQLit Closed")

# # Different DataTypes

# import sqlite3

# conn = sqlite3.connect("demo.db")

# conn.execute('''CREATE TABLE person
#              (NAME TXT, 
#               AGE INTEGER,
#               WEIGHT REAL);''')

# conn.execute('''INSERT INTO person VALUES('Yousuf',21,81.5)''')

# cursor = conn.execute('''SELECT * FROM person;''')
# for i in cursor:
#     print(str(i[0])+" "+str(i[1])+" "+str(i[2]))
#     print(str(type(i[0]))+" "+str(type(i[1]))+" "+str(type(i[2])))

# # Cursor

# import sqlite3

# conn = sqlite3.connect("hotel.db")
# cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS hotel
#                (FIND INTEGER PRIMARY KEY NOT NULL,
#                FNAME TEXT NOT NULL,
#                COST INTEGER NOT NULL,
#                WEIGHT INTEGER NOT NULL)''')

# cursor.execute('''INSERT INTO hotel(FIND,FNAME,COST,WEIGHT) VALUES(1,'Cake',800,10)''')
# cursor.execute('''INSERT INTO hotel(FIND,FNAME,COST,WEIGHT) VALUES(2,'Biscuits',100,20)''')
# cursor.execute('''INSERT INTO hotel(FIND,FNAME,COST,WEIGHT) VALUES(3,'Chocos',1000,30)''')

# conn.commit()
# print("Data inserted Successfully")
# conn.close()

# # Retreive All the table values
# import sqlite3

# conn = sqlite3.connect("hotel.db")
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM hotel")

# rows = cursor.fetchall()

# print("All food items:\n")
# for row in rows:
#     print(f"FOOD ID: {row[0]}, Name: {row[1]}, Cost: {row[2]}, Weight: {row[3]}")

# cursor.close()

# # Retrieve Only the selected values

# import sqlite3

# conn = sqlite3.connect("hotel.db")
# cursor = conn.cursor()

# cursor.execute('''SELECT FIND,FNAME FROM hotel;''')

# for row in cursor.fetchall():
#     print(f"FOOD ID: {row[0]}, FOOD NAME: {row[1]}")

# conn.close()

# # Another Table Creation

# import sqlite3

# conn = sqlite3.connect("hotel1.db")
# cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS hotel
#                (FIND INT PRIMARY KEY NOT NULL,
#                FNAME VARCHAR(255) NOT NULL,
#                COST INT NOT NULL,
#                WEIGHT INT NOT NULL)''')                # Create the table 

# cursor.execute('''INSERT INTO hotel(FIND,FNAME,COST,WEIGHT) VALUES(1,'Cake',800,10)''')     # Insert using specifying columns names and values
# cursor.execute('''INSERT INTO hotel(FNAME,WEIGHT,FIND,COST) VALUES('Biscuits',20,2,100)''') # Insert using specifying columns names and values and interchanging the column name does not affect the table
# cursor.execute('''INSERT INTO hotel VALUES(3,'Chocos',1000,30)''')                          # Insert using values only

# conn.commit()                            # Commit the changes
# print("Data inserted Successfully")
# conn.close()                             # Closing the connection

# import sqlite3

# conn = sqlite3.connect("hotel1.db")
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM hotel ")

# rows = cursor.fetchall()
# # rows = cursor.fetchmany(2)
# # rows = cursor.fetchone()

# print("All food items:\n")
# for row in rows:
#     print(f"FOOD ID: {row[0]}, Name: {row[1]}, Cost: {row[2]}, Weight: {row[3]}")

# conn.close()

# # Using ORDER BY

# import sqlite3

# conn = sqlite3.connect("hotel1.db")
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM hotel ORDER BY COST")

# rows = cursor.fetchall()

# print("All food items:\n")
# for row in rows:
#     print(f"FOOD ID: {row[0]}, Name: {row[1]}, Cost: {row[2]}, Weight: {row[3]}")

# conn.close()

# # LIMIT clause

import sqlite3

conn = sqlite3.connect("hotel1.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM hotel LIMIT 2")

rows = cursor.fetchall()

print("All food items:\n")
for row in rows:
    print(f"FOOD ID: {row[0]}, Name: {row[1]}, Cost: {row[2]}, Weight: {row[3]}")

conn.close()