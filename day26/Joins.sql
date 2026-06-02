-- CREATE TABLE StudentDetails (
--     id INT PRIMARY KEY,
--     sname VARCHAR(50),
--     age INT,
--     university VARCHAR(100)
-- );

-- INSERT INTO StudentDetails (id, sname, age, university)
-- VALUES
-- (1, 'Girish', 24, 'IIT Hyderabad'),
-- (2, 'Aaditya', 24, 'SRM University'),
-- (3, 'Aashish', 23, 'IIT Hyderabad'),
-- (4, 'John', 25, 'Mumbai University'),
-- (5, 'Shruti', 24, 'IIT Hyderabad'),
-- (6, 'Leena', 25, 'Mumbai University');

-- CREATE TABLE CourseDetails (
--     cid INT PRIMARY KEY,
--     cname VARCHAR(100),
--     ratings DECIMAL(2,1),
--     price INT
-- );

-- INSERT INTO CourseDetails (cid, cname, ratings, price)
-- VALUES
-- (1, 'Python Fundamentals', 4.6, 2999),
-- (2, 'Machine Learning', 4.3, 1999),
-- (3, 'DSA A-Z', 4.9, 5999),
-- (4, 'Competitive Programming', 4.7, 4999),
-- (5, 'Android Programming', 4.6, 4999);

-- CREATE TABLE EnrolledIn (
--     sid INT,
--     cid INT,
--     PRIMARY KEY (sid, cid),
--     FOREIGN KEY (sid) REFERENCES StudentDetails(id),
--     FOREIGN KEY (cid) REFERENCES CourseDetails(cid)
-- );

-- INSERT INTO EnrolledIn (sid, cid)
-- VALUES
-- (1, 3),
-- (1, 4),
-- (2, 1),
-- (2, 3),
-- (3, 3),
-- (4, 1);

-- SELECT * FROM coursedetails;
-- SELECT * FROM enrolledin;
-- SELECT * FROM studentdetails;

-- INNER JOIN

SELECT s.id, s.sname, s.age FROM studentdetails s INNER JOIN enrolledin e ON s.id = e.sid INNER JOIN coursedetails c ON c.cid = e.cid WHERE c.cname = "Python Fundamentals";

SELECT c.cname, COUNT(*) FROM studentdetails s INNER JOIN enrolledin e ON s.id = e.sid INNER JOIN coursedetails c ON c.cid = e.cid GROUP BY cname HAVING COUNT(*) > 1;

SELECT DISTINCT (s.id), s.sname, s.age FROM studentdetails s INNER JOIN enrolledin e ON s.id = e.sid WHERE s.university = "IIT Hyderabad";

SELECT c.cname, c.price, c.ratings FROM coursedetails c INNER JOIN enrolledin e ON c.cid = e.cid WHERE c.price > 4000;

-- OUTER JOIN
-- LEFT OUTER JOIN / LEFT JOIN
USE flaskdb;

SELECT s.sname, c.cname FROM studentdetails s LEFT JOIN enrolledin e ON s.id = e.sid LEFT JOIN coursedetails c ON c.cid = e.cid;

SELECT s.sname, COUNT(c.cid) FROM studentdetails s LEFT JOIN enrolledin e ON s.id = e.sid LEFT JOIN coursedetails c ON c.cid = e.cid GROUP BY s.sname;

SELECT s.sname FROM studentdetails s LEFT JOIN enrolledin e ON s.id = e.sid WHERE e.sid IS NULL;

-- RIGHT OUTER JOIN / RIGHT JOIN

SELECT s.sname, c.cname FROM studentdetails s RIGHT JOIN enrolledin e ON s.id = e.sid RIGHT JOIN coursedetails c ON c.cid = e.cid;

SELECT s.sname, COUNT(c.cid) FROM studentdetails s RIGHT JOIN enrolledin e ON s.id = e.sid RIGHT JOIN coursedetails c ON c.cid = e.cid GROUP BY s.sname;

SELECT s.sname FROM enrolledin e RIGHT JOIN studentdetails s ON s.id = e.sid WHERE e.sid IS NULL;

-- FULL OUTER JOIN 

SELECT s.sname, COALESCE(c.cname,'NO Course') FROM studentdetails s LEFT JOIN enrolledin e ON s.id = e.sid LEFT JOIN coursedetails c ON c.cid = e.cid
UNION
SELECT COALESCE(s.sname,'NO Student'), c.cname FROM studentdetails s RIGHT JOIN enrolledin e ON s.id = e.sid RIGHT JOIN coursedetails c ON c.cid = e.cid;

SELECT s.sname, COALESCE(c.cname,'NO Course') FROM studentdetails s LEFT JOIN enrolledin e ON s.id = e.sid LEFT JOIN coursedetails c ON c.cid = e.cid
UNION
SELECT COALESCE(s.sname,'NO Student'), c.cname FROM studentdetails s RIGHT JOIN enrolledin e ON s.id = e.sid RIGHT JOIN coursedetails c ON c.cid = e.cid ORDER BY sname;

-- SELF JOIN

SELECT s1.sname AS student1, s2.sname As student2, s1.university FROM studentdetails s1 INNER JOIN studentdetails s2 ON s1.university = s2. university AND s1.id < s2.id;

SELECT s1.sname AS student1, s2.sname As student2, s1.university FROM studentdetails s1 LEFT JOIN studentdetails s2 ON s1.university = s2. university AND s1.id < s2.id;

-- CROSS JOIN

SELECT s.sname,c.cname FROM studentdetails s CROSS JOIN coursedetails c;

SELECT * FROM studentdetails CROSS JOIN coursedetails CROSS JOIN enrolledin;

-- UPDATE JOIN

UPDATE studentdetails s JOIN enrolledin e ON s.id = e.sid JOIN coursedetails c ON c.cid = e.cid SET s.age = s.age + 2 WHERE s.university = 'IIT Hyderabad';
SELECT * FROM studentdetails;