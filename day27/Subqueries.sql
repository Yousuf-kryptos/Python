CREATE DATABASE demodb;

USE demodb;

CREATE TABLE Employee(
    empid numeric(10),
    name varchar(20),
    salary numeric(10),
    department varchar(20)
);

CREATE TABLE Departments(
    deptid numeric(10),
    department varchar(20)
);

INSERT INTO Employee 
VALUES (100,"Jacob A",20000,"SALES"),(101,"James T",50000,"IT"),(102,"Riya S",30000,"IT");

INSERT INTO Departments 
VALUES (1,"IT"),(2,"ACCOUNTS"),(3,"SUPPORT");

-- SUBQUERIES

SELECT * FROM Employee WHERE department = (SELECT department FROM Departments WHERE deptid = 1);

-- > and >=

SELECT * FROM Employee WHERE salary > (SELECT AVG(salary) FROM Employee);
SELECT * FROM Employee WHERE salary >= (SELECT AVG(salary) FROM Employee);

-- IN and NOT IN

SELECT * FROM Employee WHERE department IN (SELECT department FROM Departments);
SELECT * FROM Employee WHERE department NOT IN (SELECT department FROM Departments);

-- FROM

SELECT department FROM (SELECT * FROM Employee) AS A;

-- Correlated Subquery

SELECT empid, name FROM Employee AS A WHERE salary < (SELECT AVG(salary) FROM Employee AS B WHERE A.department = B.department);

-- EXISTS and NOT EXISTS

SELECT empid, name FROM Employee AS A WHERE EXISTS (SELECT 1 FROM Departments AS B WHERE A.department = B.department);

SELECT empid, name FROM Employee AS A WHERE NOT EXISTS (SELECT 1 FROM Departments AS B WHERE A.department = B.department);