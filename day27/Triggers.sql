CREATE DATABASE triggerdb;

USE triggerdb;

-- BEFORE UPDATE TRIGGER

CREATE TABLE customer(acc_no INT PRIMARY KEY, cust_name VARCHAR(40), avail_balance DECIMAL);

CREATE TABLE mini_statement(acc_no INT, avail_balance DECIMAL, FOREIGN KEY (acc_no) REFERENCES customer(acc_no) ON DELETE cascade); -- ON DELETE CASCADE  used with foreign keys to automatically remove child records when their referenced parent record is deleted

INSERT INTO customer VALUES(1000,"Peter",7000),(1001,"Francis",12000);

delimiter //
CREATE TRIGGER update_cus
           BEFORE UPDATE ON customer
           FOR EACH ROW
           BEGIN
           INSERT INTO mini_statement VALUES(OLD.acc_no, OLD.avail_balance);
           END;
//

delimiter ;
UPDATE customer SET avail_balance = avail_balance + 3000 WHERE acc_no = 1001;
UPDATE customer SET avail_balance = avail_balance + 3000 WHERE acc_no = 1000;

SELECT * FROM mini_statement;

-- AFTER UPDATE TRIGGER

CREATE TABLE micro_statement(acc_no INT, avail_balance DECIMAL, FOREIGN KEY (acc_no) REFERENCES customer(acc_no) ON DELETE CASCADE);

INSERT INTO customer VALUES(1002,'Janitor',9000);

delimiter //
CREATE TRIGGER update_after
            AFTER UPDATE ON customer
            FOR EACH ROW
            BEGIN
            INSERT INTO micro_statement VALUES(NEW.acc_no, NEW.avail_balance);
            END;
//
delimiter ;
UPDATE customer SET avail_balance = avail_balance + 1500  WHERE acc_no = 1002;

SELECT * FROM micro_statement;

SELECT * FROM customer;

TRUNCATE TABLE micro_statement;

-- BEFORE INSERT TRIGGER

create table contacts (contact_id INT (11) NOT NULL AUTO_INCREMENT, last_name VARCHAR (30) NOT NULL, first_name VARCHAR (25), birthday DATE, created_date DATE, created_by VARCHAR(30),  CONSTRAINT contacts_pk PRIMARY KEY (contact_id)); 

delimiter //
CREATE TRIGGER contact_before_insert
             BEFORE INSERT ON contacts
             FOR EACH ROW
             BEGIN
              DECLARE vUser VARCHAR(30);
              
              SELECT USER() into vUser;
              
              SET NEW.created_date = SYSDATE();
              
              SET NEW.created_by = vUser;
			END;
//

DELIMITER ;
INSERT INTO contacts VALUES (1,'Aasik','Yousuf', str_to_date('18-05-2004','%d-%m-%Y'), str_to_date('02-06-2026','%d-%m-%Y'),"xyz"),(2,'Johnson','Fredric', str_to_date('20-07-2005','%d-%m-%Y'), str_to_date('02-06-2026','%d-%m-%Y'),"abc"); 

SELECT * FROM contacts;

-- AFTER INSERT TRIGGER

CREATE TABLE contact_audit(contact_id INT, created_date DATE, created_by VARCHAR(30));

delimiter // 
CREATE TRIGGER after_insert
              AFTER INSERT ON contacts
              FOR EACH ROW
              BEGIN
                DECLARE vUser VARCHAR(40);
                
                SELECT USER() into vUser;
                
                INSERT INTO contact_audit(contact_id,created_date,created_by) VALUES (NEW.contact_id, SYSDATE(), vUser);
			END;
//

delimiter ; 
INSERT INTO contacts VALUES (3,'Aasik','Yousuf', str_to_date('18-05-2004','%d-%m-%Y'), str_to_date('02-06-2026','%d-%m-%Y'),"xyz");

SELECT * FROM contact_audit;

-- BEFORE DELETE TRIGGER

create table IF NOT EXISTS contacts_audit (contact_id integer, deleted_date date, deleted_by varchar(20)); 

delimiter //
CREATE TRIGGER before_delete_1
			BEFORE DELETE ON contacts
            FOR EACH ROW
            BEGIN
              DECLARE vUser VARCHAR(30);
              
              SELECT USER() INTO vUser;
              
              INSERT INTO contacts_audit
              (contact_id, deleted_date, deleted_by)
              VALUES
              (OLD.contact_id,SYSDATE(),vUSer);
		   END;
//

              
delimiter ;

SHOW TRIGGERS FROM triggerdb;

INSERT INTO contacts VALUES(4,'Mohammed','Yousuf', str_to_date('18-05-2004','%d-%m-%Y'), str_to_date('02-06-2026','%d-%m-%Y'),"xyz");

DELETE FROM contacts WHERE last_name = 'Mohammed';

SELECT * FROM contacts_audit;

-- AFTER DELETE TRIGGER

create table IF NOT EXISTS contacts_audit (contact_id integer, deleted_date date, deleted_by varchar(20)); 

delimiter //
CREATE TRIGGER after_delete_1
			AFTER DELETE ON contacts
            FOR EACH ROW
            BEGIN
              DECLARE vUser VARCHAR(30);
              
              SELECT USER() INTO vUser;
              
              INSERT INTO contacts_audit
              (contact_id, deleted_date, deleted_by)
              VALUES
              (OLD.contact_id,SYSDATE(),vUSer);
		   END;
//

              
delimiter ;

INSERT INTO contacts VALUES(5,'Snow','Jon', str_to_date('18-05-2004','%d-%m-%Y'), str_to_date('02-06-2026','%d-%m-%Y'),"xyz");

DELETE FROM contacts WHERE last_name = 'Snow';

SELECT * FROM contacts_audit;

-- DEMO

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    grade CHAR(1)
);

CREATE TABLE students_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    action VARCHAR(50)
);

delimiter //

CREATE TRIGGER after_insert
              AFTER INSERT ON students
              FOR EACH ROW
              BEGIN
               INSERT INTO students_log (student_id,action) VALUES (NEW.id,'Inserted');
			  END;
//

delimiter ; 
INSERT INTO students (name,grade) VALUES ('Yousuf','A');

SELECT * FROM students_log;

-- SHOW TRIGGER

SHOW TRIGGERS FROM triggerdb;

SHOW TRIGGERs WHERE 'TABLE' = 'customer';

SELECT * FROM information_schema.TRIGGERS WHERE EVENT_MANIPULATION = 'INSERT';

SELECT * FROM information_schema.TRIGGERS WHERE ACTION_TIMING = 'BEFORE';

SHOW TRIGGERS LIKE 'contact_before%';

-- DROP TRIGGER

DROP TRIGGER IF EXISTS after_delete_1;