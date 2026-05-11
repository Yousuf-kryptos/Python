import sqlite3

conn = sqlite3.connect('delete1.db')

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS delete1")


table = """
CREATE TABLE delete1 (
    Email VARCHAR(255) NOT NULL,
    Name CHAR(25) NOT NULL,
    Score INT
);
"""
cursor.execute(table)

data = [
    ("geekk1@gmail.com", "Geek1", 25),
    ("geekk2@gmail.com", "Geek2", 15),
    ("geekk3@gmail.com", "Geek3", 36),
    ("geekk4@gmail.com", "Geek4", 27),
    ("geekk5@gmail.com", "Geek5", 40),
    ("geekk6@gmail.com", "Geek6", 14),
    ("geekk7@gmail.com", "Geek7", 10)
]

cursor.executemany("INSERT INTO delete1 (Email, Name, Score) VALUES (?, ?, ?)", data)

# cursor.execute("DELETE FROM delete1 WHERE Score < 15")

cursor.execute("DELETE FROM delete1")

cursor.execute("SELECT * FROM delete1")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()

conn.close()