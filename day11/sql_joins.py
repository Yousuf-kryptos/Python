# JOIN

import sqlite3

conn = sqlite3.connect('joins.db')

cursor = conn.cursor()

# cursor.executescript('''
# CREATE TABLE Advisor(
# AdvisorID INTEGER NOT NULL,
# AdvisorName TEXT NOT NULL,
# PRIMARY KEY(AdvisorID)
# );

# CREATE TABLE Student(
# StudentID NUMERIC NOT NULL,
# StudentName NUMERIC NOT NULL,
# AdvisorID INTEGER,
# FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
# PRIMARY KEY(StudentID)
# );

# INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES
# (1,"John Paul"), 
# (2,"Anthony Roy"), 
# (3,"Raj Shetty"),
# (4,"Sam Reeds"),
# (5,"Arthur Clintwood");

# INSERT INTO Student(StudentID, StudentName, AdvisorID) VALUES
# (501,"Geek1",1),
# (502,"Geek2",1),
# (503,"Geek3",3),
# (504,"Geek4",2),
# (505,"Geek5",4),
# (506,"Geek6",2),
# (507,"Geek7",2),
# (508,"Geek8",3),
# (509,"Geek9",NULL),
# (510,"Geek10",1);

# ''')

# # INNER JOIN
# cursor.execute('''SELECT StudentID, StudentName, AdvisorName FROM
#                Student INNER JOIN Advisor ON Advisor.AdvisorID == Student.AdvisorID''')

# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# # LEFT JOIN
# cursor.execute('''SELECT StudentID, StudentName, AdvisorName FROM
#                Student LEFT JOIN Advisor USING(AdvisorID);''')

# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# # RIGHT JOIN
# cursor.execute('''SELECT StudentID, StudentName, AdvisorName FROM
#                Student RIGHT JOIN Advisor USING(AdvisorID);''')

# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# # CROSS JOIN
# cursor.execute('''SELECT StudentID, StudentName, AdvisorName FROM
#                Student RIGHT JOIN Advisor;''')

# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# conn.commit()

# conn.close()

