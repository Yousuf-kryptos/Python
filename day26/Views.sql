-- VIEWS
-- CREATE VIEW

CREATE VIEW IITHyderabadStudentView AS
SELECT id, sname, age
FROM studentdetails
WHERE university = 'IIT Hyderabad';

SELECT * FROM iithyderabadstudentview;

CREATE VIEW view2 AS
SELECT s.sname, s.age, c.cname, c.price
FROM studentdetails s JOIN
enrolledin e ON s.id = e.sid JOIN
coursedetails c ON c.cid = e.cid;

SELECT * FROM view2;

CREATE VIEW view3 AS
SELECT sname, age
FROM studentdetails
WHERE age >24;

SELECT * FROM view3;
 
-- UPDATE VIEW

CREATE OR REPLACE VIEW IITHyderabadStudentView AS
SELECT *
FROM studentdetails
WHERE university = 'IIT Hyderabad'
WITH CHECK OPTION; -- To remove id column

SELECT * FROM IITHyderabadStudentView;

UPDATE iithyderabadstudentview SET age = 24 WHERE id = 5;

-- INSERT INTO VIEW

INSERT INTO IITHyderabadStudentView VALUES(7,"Tenali Rama",22,'IIT Hyderabad');

SELECT * FROM studentdetails;

-- DELETE FROM VIEW

DELETE FROM iithyderabadstudentview WHERE sname = 'Tenali Rama';

-- DROP VIEW

DROP VIEW pythonenrolledview;

DROP VIEW view2;

DROP VIEW IF EXISTS view3;

-- RENAME VIEW

RENAME TABLE view2 TO joinview;

SELECT * FROM joinview;

-- TEMPORARY TABLE

CREATE TEMPORARY TABLE studentdetailsTemp(
      sid INT PRIMARY KEY,
      sname VARCHAR(255),
      age INT);
      
INSERT INTO studentdetailsTemp(sid, sname, age)
SELECT id, sname, age
FROM StudentDetails 
WHERE university = "IIT Hyderabad";

DROP TEMPORARY TABLE studentdetailsTemp;
