CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2)
);

INSERT INTO employees (name, department, salary) VALUES
('John Doe', 'Sales', 55000.00),
('Jane Smith', 'Sales', 60000.00),
('Jim Brown', 'Sales', 65000.00),
('Jake White', 'Engineering', 75000.00),
('Jill Green', 'Engineering', 80000.00),
('Jenny Black', 'Engineering', 85000.00),
('James Gray', 'Marketing', 50000.00),
('Janet Blue', 'Marketing', 52000.00),
('Joan Pink', 'Marketing', 54000.00);

-- COMMON TABLE EXPRESSION (CTE)

WITH department_salaries AS(
    SELECT department, AVG(salary) AS average_salary, SUM(salary) AS total_salary
    FROM employees GROUP BY department 
    )
SELECT department, average_salary, total_salary FROM department_salaries WHERE average_salary > 60000;

SELECT department, AVG(salary) as Average, SUM(salary) FROM employees GROUP BY department HAVING Average > 60000;

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES categories(id)
);

INSERT INTO categories (name, parent_id) VALUES
('Electronics', NULL),
('Computers', 1),
('Laptops', 2),
('Desktops', 2),
('Smartphones', 1),
('Accessories', 1),
('Chargers', 6),
('Cables', 6);

-- WITH RECURSIVE category_hierarchy AS(
--      SELECT id, name, parent_id, 1 AS level
--      FROM categories
--      WHERE parent_id IS NULL
--      UNION ALL
--      SELECT c.id, c.name, c.parent_id, ch.level+1
--      FROM categories c
--      JOIN category_hierarchy ch ON c.parent_id = ch.parent_id
--      )
-- SELECT id, name, parent_id FROM category_hierarchy;

WITH RECURSIVE category_hierarchy2 AS (

    -- Anchor: start from root nodes (no parent)
    SELECT id, name, parent_id, 1 AS level
    FROM categories
    WHERE parent_id IS NULL

    UNION ALL

    -- Recursive: find children of already-found rows
    SELECT c.id, c.name, c.parent_id, ch.level + 1
    FROM categories c
    JOIN category_hierarchy2 ch ON c.parent_id = ch.id  -- ✓ fixed

)
SELECT id, name, parent_id, level
FROM category_hierarchy2
ORDER BY level, parent_id;

SELECT * FROM categories;

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    salesperson_id INT,
    sales_amount DECIMAL(10, 2)
);

INSERT INTO sales (salesperson_id, sales_amount) VALUES
(1, 3000.00),
(1, 2500.00),
(1, 1500.00),
(2, 4000.00),
(2, 2000.00),
(3, 1000.00),
(3, 2000.00),
(4, 7000.00),
(5, 3000.00),
(5, 2500.00);

-- TEMPORARY AGGREGATION

WITH total_sales AS(
    SELECT salesperson_id, SUM(sales_amount) AS total_sales
    FROM sales
    GROUP BY salesperson_id
    )
SELECT salesperson_id, total_sales FROM total_sales WHERE total_sales > 5000;

