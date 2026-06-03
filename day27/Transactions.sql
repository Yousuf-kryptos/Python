-- CREATE TABLE accounts (
--     account_id INT PRIMARY KEY,
--     account_name VARCHAR(100),
--     balance DECIMAL(10, 2)
-- );

-- INSERT INTO accounts (account_id, account_name, balance) VALUES
-- (1, 'Alice', 1000.00),
-- (2, 'Bob', 500.00);

-- TRANSACTION

START TRANSACTION;

SAVEPOINT savepoint1;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

SAVEPOINT savepoint2;
UPDATE accounts SET balance = balance + 50  WHERE account_id = 1;
UPDATE accounts SET balance = balance - 50  WHERE account_id = 2;

-- Roll back only to savepoint1 (undoes savepoint2 changes too)
ROLLBACK TO SAVEPOINT savepoint1;

-- Check result
SELECT * FROM accounts;

-- End the transaction
COMMIT;

