SELECT * FROM customer;

delimiter //

CREATE PROCEDURE read_customers1()
            BEGIN
             DECLARE done INT DEFAULT 0;
             DECLARE vName VARCHAR(40);
             DECLARE vBal DECIMAL;
             
             DECLARE cur CURSOR FOR 
                 SELECT cust_name, avail_balance FROM customer;
                 
			DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
             
             CREATE TEMPORARY TABLE IF NOT EXISTS temp_results(
               customer_name VARCHAR(40),
               balance DECIMAL);
             
             OPEN cur;
             
			 row_loop : LOOP
               FETCH cur INTO vName, vBal;
               IF done = 1 THEN
                  LEAVE row_loop;
			   END IF;
              
               INSERT INTO temp_results VALUES (vName,vBal);
			END LOOP;
            
            CLOSE cur;
            SELECT * FROM temp_results;
            
            DROP TEMPORARY TABLE temp_results;
END;
//

delimiter ;

CALL read_customers1();

delimiter //

CREATE PROCEDURE bonus_update()
        BEGIN
        DECLARE done INT DEFAULT 0;
        DECLARE v_acc INT;
        DECLARE v_bal DECIMAL;
        
        DECLARE cur CURSOR FOR
            SELECT acc_no, avail_balance FROM customer;
            
		DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
        
        OPEN cur;
        
        row_loop : LOOP
            FETCH cur INTO v_acc, v_bal;
            IF done = 1 THEN
                LEAVE row_loop;
			END IF;
            
            IF v_bal >10000 THEN
               UPDATE customer SET avail_balance = avail_balance * 1.10 WHERE v_acc = acc_no;
			END IF;
		END LOOP;
        
        CLOSE cur;
        
END;
 //

CALL bonus_update();//
SELECT * FROM customer;
              