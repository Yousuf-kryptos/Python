-- CREATE TABLE students(student_id INT PRIMARY KEY, student_name VARCHAR(100), birth_date VARCHAR(100), branch VARCHAR(10), state VARCHAR(25));

-- INSERT INTO students(student_id, student_name, birth_date, branch, state) VALUES(19401, 'JOHN', '1999-03-17', 'CSE', 'CALIFORNIA'),
-- (19402, 'MICHAEL', '2000-08-07', 'ECE', 'TEXAS'),
-- (19403, 'DAVID', '2000-03-10', 'ECE', 'FLORIDA'),
-- (19404, 'ROBERT', '1999-03-15', 'CSE', 'NEW YORK'),
-- (19405, 'JAMES', '2000-04-19', 'CSE', 'ILLINOIS'),
-- (19406, 'MIKE', '2000-01-29', 'IT', 'NEW YORK');

-- SELECT * FROM students;

-- AND, OR and NOT

-- AND operator
SELECT * FROM students WHERE branch = 'CSE' AND state = 'CALIFORNIA';

-- OR operator
SELECT * FROM students WHERE branch = 'CSE' OR branch = 'ECE';

-- NOT operator
SELECT * FROM students WHERE NOT state = 'TEXAS';

-- LIKE Operator

SELECT * FROM students;

SELECT * FROM students WHERE student_name LIKE 'J%'; -- Names start with 'J'

SELECT * FROM students WHERE state LIKE '%IA'; -- Ends with 'IA'

SELECT * FROM students WHERE student_name LIKE '%CH%'; -- names containing 'CH'

SELECT * FROM students WHERE state LIKE '__X%'; -- containing X as third letter from first

SELECT * FROM students WHERE student_name LIKE '%R_'; -- containing R as second letter from last

-- IN Operator

SELECT student_name, birth_date, branch, state FROM students WHERE branch IN('CSE','IT');

SELECT * FROM students WHERE state NOT IN('TEXAS','NEW YORK');

-- ALTER TABLE students ADD COLUMN age INT;

-- UPDATE students SET age = 25 WHERE student_id = 19406;

-- IS NULL Operator

SELECT * FROM students WHERE age IS NULL;

SELECT COUNT(*) FROM students WHERE age IS NULL;

UPDATE students SET age = 18 WHERE age IS NULL;

SELECT * FROM students;

DELETE FROM students WHERE age IS NULL;

SELECT * FROM customers;
SELECT * FROM employees;

-- UNION Operator

SELECT name, 'Customers' as type FROM customers UNION SELECT name, 'Employees' FROM employees ORDER BY name;

SELECT name, 'Customers' as type FROM customers WHERE age >25 UNION SELECT name, 'Employees' FROM employees WHERE salary > 50000 ORDER BY name;

-- UNION ALL Operator
-- It doesn't remove duplicate values

SELECT name, department FROM employees WHERE department = 'IT' UNION ALL SELECT name, city FROM customers WHERE city = 'Los Angeles';

SELECT name, department FROM employees WHERE department = 'IT' UNION ALL SELECT name, city FROM customers WHERE city = 'Los Angeles' ORDER BY 2;

-- BETWEEN Operator

SELECT * FROM employees WHERE salary BETWEEN 55000 AND 75000;

SELECT * FROM employees WHERE name BETWEEN 'A' AND 'I';

SELECT * FROM employees WHERE salary NOT BETWEEN 55000 AND 75000;

-- ANY and ALL Operator
SELECT * FROM employees;	

-- ANY Operator
SELECT name, salary FROM employees WHERE salary > ANY(SELECT salary FROM employees WHERE department = 'IT');

SELECT name, salary FROM employees WHERE salary > ANY(SELECT salary FROM employees WHERE department = 'IT')ORDER BY salary DESC; -- Using ORDER BY

-- ALL Operator
SELECT name, salary FROM employees WHERE salary > ALL(SELECT salary FROM employees WHERE department = 'IT');

SELECT department, MIN(salary) FROM employees GROUP BY department HAVING MIN(salary) > ALL(SELECT salary FROM employees WHERE salary <= 50000);

-- ALTER TABLE products ADD COLUMN product_id INT;

-- UPDATE products SET product_id = 101 WHERE product = 'Laptop' ;

-- UPDATE products SET product_id = 178 WHERE product = 'Mouse' ;

-- UPDATE products SET product_id = 190 WHERE product = 'keyboard' ;

-- UPDATE products SET product_id = 192 WHERE product = 'Headphones' ;

UPDATE products SET product = 'Monitor' WHERE product_id = 190 ;

-- SELECT * FROM products;
-- SELECT * FROM orders;

-- EXISTS

SELECT order_id, order_name FROM orders WHERE EXISTS (SELECT products.product_id FROM products WHERE orders.customer_id = products.product_id);

-- INTERSECT

SELECT customer_id, order_name FROM orders WHERE customer_id IN (SELECT product_id FROM products );

SELECT DISTINCT product_id, product FROM products INNER JOIN orders ON products.product_id = orders.customer_id;

-- AGGREGATE FUNCTIONS

-- COUNT()

SELECT * FROM employees;

SELECT COUNT(*) AS total_employees FROM employees;

SELECT COUNT(DISTINCT department) AS No_of_dept FROM employees;

-- SUM()

SELECT SUM(salary) AS total_salary FROM employees;

SELECT SUM(salary) AS total_salary FROM employees WHERE department = 'IT';

SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department;

SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department HAVING total_salary > 200000;

SELECT SUM(DISTINCT salary) AS total_salary FROM employees;

-- MIN()

SELECT MIN(salary) FROM employees;	

SELECT MIN(salary) FROM employees WHERE salary > 55000;

SELECT department, MIN(salary) FROM employees GROUP BY department;

-- MAX()

SELECT MAX(salary) FROM employees;

SELECT MAX(birth_date) FROM students;

SELECT * FROM students;

SELECT MAX(age) FROM students WHERE birth_date > '1999-03-15';

-- AVG()

SELECT AVG(salary) FROM employees;

SELECT * FROM employees WHERE salary >(SELECT AVG(salary) FROM employees);

SELECT AVG(salary), department FROM employees GROUP BY department;

