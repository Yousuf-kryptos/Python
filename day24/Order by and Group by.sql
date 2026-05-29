-- ORDER BY

SELECT * FROM customers;

SELECT name,age FROM customers ORDER BY age ASC;

SELECT name,age FROM customers ORDER BY age DESC;

SELECT * FROM customers ORDER BY name,age DESC;

-- GROUP BY

-- CREATE TABLE employees (
--     id INT PRIMARY KEY,
--     name VARCHAR(50),
--     department VARCHAR(50),
--     salary INT
-- );

-- INSERT INTO employees (id, name, department, salary) VALUES
-- (1, 'Alice', 'HR', 60000),
-- (2, 'Bob', 'IT', 50000),
-- (3, 'Charlie', 'IT', 70000),
-- (4, 'David', 'Marketing', 40000),
-- (5, 'Eva', 'Finance', 80000),
-- (6, 'Frank', 'HR', 55000),
-- (7, 'Grace', 'IT', 65000),
-- (8, 'Alice', 'IT', 60000),
-- (9, 'Bob', 'HR', 50000),
-- (10, 'Charlie', 'IT', 70000),
-- (11, 'David', 'Marketing', 40000),
-- (12, 'Eva', 'Finance', 80000),
-- (13, 'Frank', 'HR', 55000),
-- (14, 'Grace', 'IT', 65000),
-- (15, 'Hannah', 'Marketing', 45000),
-- (16, 'Isaac', 'Finance', 75000),
-- (17, 'Jack', 'IT', 62000),
-- (18, 'Kate', 'HR', 53000),
-- (19, 'Liam', 'Marketing', 47000);

-- SELECT * FROM EMPLOYEES;

SELECT department, AVG(salary) as average_salary FROM employees GROUP BY department;

SELECT department, name, AVG(salary) as average_salary FROM employees GROUP BY department,name;

SELECT department, COUNT(*) as employee_count FROM employees GROUP BY department;

SELECT department, SUM(salary) as total_salary FROM employees GROUP BY department;

SELECT department, MIN(salary) as min_salary FROM employees GROUP BY department;

SELECT department, MAX(salary) as max_salary FROM employees GROUP BY department;