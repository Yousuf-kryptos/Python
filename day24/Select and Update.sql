USE flaskdb;

-- SELECT Statement
CREATE TABLE employees (
     employee_id INT PRIMARY KEY,
     first_name VARCHAR(50),
     last_name VARCHAR(50),
     salary DECIMAL(10, 2) );
INSERT INTO employees VALUES
     (1, 'John', 'Doe', 50000),
     (2, 'Jane', 'Smith', 60000),
     (3, 'Robert', 'Johnson', 75000);
     
CREATE TABLE customers (
     id INT PRIMARY KEY,
     name VARCHAR(50),
     contact VARCHAR(50));
INSERT INTO customers VALUES
     (101, 'John', 5000076589),
     (156, 'Jane', 6000012345),
     (178, 'Robert', 7500056789);
     
CREATE TABLE orders (
     order_id INT AUTO_INCREMENT PRIMARY KEY,
     customer_id INT,
     order_name VARCHAR(50),
     order_price INT);
INSERT INTO orders VALUES
     (1,101, 'Laptop', 50000),
     (2,156, 'Mobile', 60000),
     (3,156, 'Headphones', 75000),
     (4,178, 'Tablet', 15000),
     (5,190, 'Monitor',20000);

SELECT * FROM employees;

SELECT first_name, last_name FROM employees;

SELECT DISTINCT salary FROM employees;

SELECT INSERT("YousufAasik",9,5,"MySql") AS NewString; -- INSERT() Function

-- UPDATE statement

UPDATE employees SET salary = 70000 WHERE employee_id = 3;

UPDATE employees SET first_name = 'Rob',last_name = 'John' WHERE employee_id = 3;

UPDATE employees SET salary = salary+5000;

SELECT * FROM employees;

UPDATE IGNORE employees SET first_name = 'Robert' WHERE employee_id = 3;

-- DELETE

DELETE FROM employees WHERE employee_id = 3;

SELECT * FROM employees;

DELETE FROM employees;

DELETE customers,orders FROm customers INNER JOIN orders ON customers.id = orders.customer_id WHERE customers.id = 156;

SELECT * FROM customers;

SELECT * FROM orders;

-- DELETE Duplicate rows

SELECT DISTINCT customer_id FROM orders;

SELECT customer_id FROM orders GROUP BY customer_id;

SELECT customer_id FROM orders GROUP BY customer_id HAVING count(*) > 1;