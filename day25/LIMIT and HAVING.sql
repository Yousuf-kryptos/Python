-- LIMIT clause
use flaskdb;

SELECT * FROM employees LIMIT 3; -- Return first 3 rows

SELECT * FROM employees LIMIT 1,3; -- Return first 3 rows with starting from 2nd row

SELECT * FROM employees ORDER BY id DESC LIMIT 2; -- Return last 2 records

-- CREATE TABLE products(id INT PRIMARY KEY, product VARCHAR(100), quantity INT, price DECIMAL(10,2));

-- INSERT INTO products(id, product, quantity, price) VALUES (1, 'Laptop', 2, 1000),
-- (2, 'Mouse', 10, 20),
-- (3, 'Laptop', 3, 1000),
-- (4, 'Mouse', 6, 20),
-- (5, 'Keyboard', 5, 50),
-- (6, 'Headphones', 5, 800),
-- (7, 'Mouse', 6, 20);

-- HAVING Clause

SELECT product, COUNT(*) FROM products GROUP BY product HAVING COUNT(*) > 1;

SELECT product, SUM(quantity) FROM products GROUP BY product HAVING SUM(quantity) > 10;

