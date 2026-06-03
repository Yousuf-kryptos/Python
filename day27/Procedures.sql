USE triggerdb;

create table author (author_id integer primary key, 
                            authorName varchar(30), 
                            email varchar (25), gender varchar (6));

create table book (BookId integer not null unique, 
                        ISBN integer primary key, 
                       book_name varchar (30) not null, 
                        author integer, ed_num integer, 
                      price integer, pages integer, 
         foreign key (author) references author (author_id) on delete cascade);
         
insert into author values 
              (1, "Kraig Muller", "Wordnewton@gmail.com", "Male");
insert into author values
              (2, "Karrie Nicolette", "karrie23@gmail.com", "Female");
insert into book values
              (1, 001, "Glimpses of the past", 1, 1, 650, 396);
insert into book values
              (2, 002, "Beyond The Horizons of Venus", 1, 1, 650, 396);
insert into book values
              (3, 003, "Ultrasonic Aquaculture", 2, 1, 799, 500);
insert into book values
              (4, 004, "Cryogenic Engines", 2, 1, 499, 330); 
              
-- PROCEDURES
-- PROCEDURE WITH NO PARAMETERS
delimiter //
CREATE PROCEDURE display_book()
                 BEGIN
                 SELECT * FROM book;
                 END;
//
                 
call display_book();//

-- PROCEDURE WITH IN PARAMETER
delimiter //
CREATE PROCEDURE update_price(IN temp_ISBN VARCHAR(20), IN new_price INT)
                           BEGIN
                           UPDATE book SET price = new_price WHERE ISBN = temp_ISBN;
                           END;
//

call update_price(2,700);//

SELECT * FROM book;

-- PROCEDURE WITH OUT PARAMETER

delimiter //

CREATE PROCEDURE disp_max(OUT highestprice INT)
                   BEGIN
                   SELECT MAX(price) into highestprice FROM book;
                   END;
//

call disp_max(@M);//

SELECT @M;

-- PROCEDURE WITH IN-OUT PARAMETER

delimiter // 

CREATE PROCEDURE disp_gender_1(INOUT mfgender VARCHAR(20), IN emp_gender VARCHAR(20))
                          BEGIN
                          SELECT count(gender) INTO mfgender FROM author WHERE gender = emp_gender;
                          END;
//

call disp_gender_1(@m,'Male');//
SELECT(@m);

call disp_gender_1(@f,'Female');//
SELECT(@f);