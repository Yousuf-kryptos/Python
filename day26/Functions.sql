-- Functions
-- DATE()

SELECT DATE('2026-06-02 12:18:26');

SELECT DATE("The date is 2026-06-02");

-- STRING Functions
-- CONCAT_WS()

SELECT CONCAT_WS(',','apple','orange') AS Concatenated_string;

-- CONCAT()

SELECT CONCAT('apple', ' ', 'orange') AS Concatenated_string;

-- CHARACTER_LENGTH()

SELECT CHARACTER_LENGTH('Hello World') AS Lenght;

-- ELT()

SELECT ELT(3,'apple', 'orange','Grape') AS Selected_string;

-- EXPORT_SET()

SELECT EXPORT_SET(5, 2, '0', ',', '1') AS Binary_set;

-- FIELD()

SELECT FIELD('banana','apple','banana','grape') AS Position;

-- FIND_IN_SET()

SELECT FIND_IN_SET('grape','apple,banana,grape') AS Position;

-- FORMAT

SELECT FORMAT(1234567.89,2) AS Formatted_number;

-- FROM_BASE64

SELECT FROM_BASE64('SGVsbG8gV29ybGQ=') AS Decoded_String;

-- HEX()

SELECT HEX('Hello') AS HEX_VALUE;

-- INSERT()

SELECT INSERT('Hello World',7,0,'Beautiful ') AS Inserted_String;

-- INSTR()

SELECT INSTR('hello World','Wor') AS Position;

-- LOWER()

SELECT LOWER('Hello World') AS Lower_string;

-- LPAD()

SELECT LPAD('Hello',10,'*') AS Padded_string;

-- LTRIM()

SELECT LTRIM('      Hello      ') AS Left_trimmed;

-- MAKE_SET()

SELECT MAKE_SET(1,'a','b','c') AS SET_VALUES;

-- MID()

SELECT MID('Hello World',7,5) AS Extracted_string;

-- OCTET_LENGTH()

SELECT OCTET_LENGTH('Hello World') AS byte_length;

-- OCT()

SELECT OCT(42) AS Octal_number;

-- ORD()

SELECT ORD('a') AS unicode_Code;

-- POSITION()

SELECT POSITION('bar' IN 'foobarbar') AS position;

-- QUOTE()

SELECT QUOTE('It\'s a beautiful day') AS Quoted_String;

-- REPLACE()

SELECT REPLACE('Hello World','World','Universe') AS Replaced_String;

-- REPEAT()

SELECT REPEAT('Hello',3) AS Repeated_string;

-- RIGHT()

SELECT RIGHT('Hello World',5) AS RightmostString;

-- RPAD()

SELECT RPAD('hello',10,'*') AS Padded_String;

-- RTRIM

SELECT RTRIM('      Hello       ') AS Trimmed_String;

-- SOUNDEX

SELECT SOUNDEX('hello') as Soundex_value;

-- MATH FUNCTION
-- ABS()

SELECT ABS(-10);

-- CEIL() OR CEILING()

SELECT CEIL(4.3);

-- FLOOR()

SELECT FLOOR(5.7);

-- ROUND()

SELECT ROUND(123.456,2);

-- POW()

SELECT POW(2,3);

-- SQRT()

SELECT SQRT(16);

-- EXP()

SELECT EXP(1);

-- LOG()

SELECT LOG(10);

-- RAND()

SELECT RAND();

-- SIN()

SELECT SIN(PI()/2);

-- COS()

SELECT COS(0);

-- TAN()

SELECT TAN(PI()/4);

-- JSON FUNCTIONS

SELECT JSON_OBJECT('name','Yousuf','age',22,'city','Chennai');

SELECT JSON_EXTRACT('{"name":"Yousuf","age":22,"city":"Chennai"}','$.age');

SELECT JSON_SET('{"name":"Yousuf","age":22,"city":"Chennai"}','$.age',21);

SELECT JSON_ARRAY('Yousuf',22,'Good');

SELECT JSON_MERGE('{"name":"Yousuf"}','{"age":22}');

SELECT JSON_REMOVE('{"name":"Yousuf","age":22}','$.age');

SELECT JSON_ARRAY_APPEND('["Yousuf",22]','$','Good');

SELECT JSON_SEARCH('{"name":"Yousuf","age":22}','one','Yousuf');

-- LTRIM()

SELECT '      Good Morning' AS Original_String, LTRIM('      Good Morning') AS Trimmed_string;

CREATE TABLE Employee
(
 Employee_id INT AUTO_INCREMENT,  
 Employee_name VARCHAR(100) NOT NULL,
 Joining_Date DATE NOT NULL,
 PRIMARY KEY(Employee_id )
);

INSERT INTO Employee
(Employee_name, Joining_Date )
VALUES
 ('     Ananya Majumdar', '2000-01-11'),
 ('   Anushka Samanta', '2002-11-10' ),
 ('   Aniket Sharma ', '2005-06-11' ),
 ('   Anik Das', '2008-01-21'  ),
 ('  Riya Jain', '2008-02-01' ),
 ('    Tapan Samanta', '2010-01-11' ),
 ('   Deepak Sharma', '2014-12-01'  ),
 ('   Ankana Jana', '2018-08-17'),
 ('  Shreya Ghosh', '2020-09-10') ;
 
 SELECT * FROM employee;
 
 SELECT Employee_id, Employee_name, LTRIM(Employee_name) AS Trimmed_name FROM employee;
 
 -- UPPER()
 
SELECT UCASE('Hello World') as UPPER_TEXT;
 
SELECT UPPER('Hello World') as UPPER_TEXT;

SET @str = BINARY "YOUSUF";

-- RTRIM()

SELECT 'MYSQL      ' AS originalString, RTRIM('MYSQL      ') AS Trimmed_string;

CREATE TABLE Student
(
  Student_id INT AUTO_INCREMENT,  
  Student_name VARCHAR(100) NOT NULL,
  Student_Class VARCHAR(20) NOT NULL,
  PRIMARY KEY(Student_id )

);

INSERT INTO Student
(Student_name, Student_Class )
VALUES
  ('Ananya Majumdar     ', 'IX'),
  ('Anushka Samanta    ', 'X' ),
  ('Aniket Sharma   ', 'XI' ),
  ('Anik Das      ', 'X'  ),
  ('Riya Jain   ', 'IX' ),
  ('Tapan Samanta    ', 'X' ),
  ('Deepak Sharma    ', 'X'  ),
  ('Ankana Jana    ', 'XII'),
  ('Shreya Ghosh    ', 'X') ;
  
SELECT * FROM student;

SELECT Student_id, Student_name, RTRIM(Student_name) as Trimmed_string FROM student;

-- CASE

SELECT name, department, salary,
CASE
    WHEN salary > 70000 THEN 'HIGH SALARY'
    WHEN salary BETWEEN 50000 AND 70000 THEN 'MID LEVEL SALARY'
    ELSE 'Low Salary'
END AS salary_status
FROM employees;

SELECT name, department,
CASE
    WHEN department = 'IT' THEN 'IT Team'
    WHEN department = 'Finance' THEN 'Accounts Team'
    WHEN department = 'HR' THEN 'Human Resource'
    ELSE 'Market Team'
END AS department_wise
FROM employees;

SELECT name, salary
FROM employees
ORDER BY 
CASE 
   WHEN salary >= 70000 THEN 1
   WHEN salary >= 50000 THEN 2
   ELSE 3
END;

-- CAST()

SELECT CAST("2026-06-02" AS DATE);

SELECT CAST(121 AS CHAR);

SELECT CAST(2-4 AS SIGNED);

SELECT CAST(2-4 AS UNSIGNED);

CREATE TABLE Orderss (
   OrderID int NOT NULL,
   CustomerName varchar(255) NOT NULL,
   OrderDate datetime NOT NULL
);

INSERT INTO Orderss (OrderID, CustomerName, OrderDate)
VALUES (1, 'John Doe', CAST('2023-03-15' AS DATE)),
       (2, 'Jane Smith', CAST('2022-04-10' AS DATE)),
       (3, 'Bob Johnson', CAST('2020-05-20' AS DATE)),
       (4, 'Alice Brown', CAST('2022-06-05' AS DATE));

SELECT OrderID, CustomerName, OrderDate
FROM Orderss
WHERE (OrderDate) = 2022
ORDER BY OrderDate DESC;

SELECT * FROM orderss;

DROP TABLE orderss;