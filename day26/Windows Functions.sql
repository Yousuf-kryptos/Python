-- WINDOW FUNCTIONS

SELECT * FROM employees;

-- ROW_NUMBER()

SELECT name, 
       department, 
       salary,
       ROW_NUMBER() OVER(PARTITION BY department ORDER BY SALARY DESC) AS row_num
FROM employees;

-- RANK() AND DENSE_RANK()

SELECT name, 
       department, 
       salary,
       RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS rank_num,
       DENSE_RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS dense_rank_num
FROM employees;

-- SUM()

SELECT id,
       name,
       salary,
       SUM(salary) OVER(ORDER BY id) AS total_Salary
FROM employees;

SELECT id,
       name,
       salary,
       SUM(salary) OVER(PARTITION BY department ORDER BY salary DESC) AS total_Salary
FROM employees; -- Department wise Salary Total

-- AVG()

SELECT id,
       name,
       salary,
       AVG(salary) OVER(ORDER BY id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS total_Salary
FROM employees; -- Take avg from current row and previous two rows

SELECT id,
       name,
       salary,
       AVG(salary) OVER(ORDER BY id) AS total_Salary
FROM employees;

-- LEAD() and LAG()

SELECT name,
       salary,
       LEAD(salary) OVER(ORDER BY id) AS next_salary,
       LAG(salary) OVER(ORDER BY id) AS previous_salary
FROM employees;

-- ROWS AND RANGE

SELECT id,
       name,
       salary,
       AVG(salary) OVER(ORDER BY id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS total_Salary
FROM employees; -- Take avg from current row and previous two rows

SELECT id,
       name,
       salary,
       SUM(salary) OVER(ORDER BY salary RANGE BETWEEN 1000 PRECEDING AND CURRENT ROW) AS total_Salary
FROM employees; -- Take avg from current row and previous two rows