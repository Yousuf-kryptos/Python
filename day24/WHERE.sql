-- SELECT * FROM customers;

-- ALTER TABLE customers ADD COLUMN city VARCHAR(100);

-- ALTER TABLE customers ADD COLUMN age INT;

-- TRUNCATE customers;

-- ALTER TABLE customers DROP COLUMN contact;

-- INSERT INTO customers VALUE (1,'John Doe','New York',30),(2,'Jane Smith','Los Angeles',25),(3,'Robert Johnson','New York',35),(4,'Alice Brown','Chicago',28),(5,'Charlie Wilson','Los Angeles',40)

SELECT * FROM customers WHERE city = 'New York'; -- Filter by single condition

SELECT * FROM customers WHERE city = 'Los Angeles' AND age < 30; -- WHERE with AND operator

SELECT * FROM customers WHERE city = 'New York' OR age > 35; -- WHERE with OR operator

SELECT * FROM customers WHERE name LIKE 'J%'; -- WHERE with LIKE operator

SELECT * FROM customers WHERE city IN ('Chicago','New York'); -- WHERE with IN clause

SELECT * FROM customers WHERE city = 'New York' ORDER BY age DESC; -- WHERE with ORDER BY
