-- Constraints

-- NOT NULL

ALTER TABLE orders MODIFY COLUMN customer_id INT NOT NULL;

CREATE TABLE views(video_name VARCHAR(255) NOT NULL, total_no_views INT);

INSERT INTO views VALUES(NULL, 255);

-- UNIQUE

ALTER TABLE orders MODIFY COLUMN order_id INT UNIQUE;

CREATE TABLE views(video_name VARCHAR(255) NOT NULL, total_no_views INT, owner VARCHAR(255) UNIQUE);

INSERT INTO views VALUES('Beast Games', 255,'Mr.beast'),('Cooking', 200,'Mr.beast');

ALTER TABLE views DROP INDEX owner; -- TO drop the UNIQUE constraints

-- CHECK 

ALTER TABLE employees ADD CONSTRAINT chk_validity  CHECK (salary >10000);

SELECT * FROM employees;
INSERT INTO employees VALUES(21,'Aasik','HR',9500);
INSERT INTO employees VALUES(20,'Yousuf','IT',15000);

ALTER TABLE employees DROP CONSTRAINT chk_validity;

CREATE TABLE views(video_name VARCHAR(255) NOT NULL, total_no_views INT, owner VARCHAR(255) UNIQUE,CHECK (total_no_views >100));

INSERT INTO views VALUES('Beast Games', 255,'Mr.beast'),('Cooking', 90,'Mr.beat');

-- DEFAULT

CREATE TABLE views(video_name VARCHAR(255) NOT NULL, total_no_views INT DEFAULT 50, owner VARCHAR(255) UNIQUE);

ALTER TABLE customers ALTER city SET DEFAULT 'NEW York';

-- PRIMARY KEY

CREATE TABLE books (book_id INT AUTO_INCREMENT, name VARCHAR(255) UNIQUE, cost INT NOT NULL, PRIMARY KEY(book_id));

INSERT INTO books VALUES(1,'Harry Potter',2500),(2,'Game of Thrones',3000);

ALTER TABLE customers DROP PRIMARY KEY; -- TO Drop the Primary Key

ALTER TABLE customers ADD PRIMARY KEY (id); -- To add the primary key

-- FOREIGN KEY

CREATE TABLE library(genre VARCHAR(255), book_id INT, no_of_books INT,FOREIGN KEY (book_id) REFERENCES books(book_id));

INSERT INTO library (genre, book_id, no_of_books)
VALUES
('Fantasy', 1, 10),
('Fantasy', 2, 5);

SELECT * FROM library;

SELECT * FROM books;

INSERT INTO library VALUES ('thriller',3,15);

ALTER TABLE library DROP FOREIGN KEY book_id;
