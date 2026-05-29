USE flaskdb;

-- RENAMING THE TABLE

RENAME TABLE products TO orders;

SELECT * FROM orders;

ALTER TABLE orders RENAME TO products;

SELECT * FROM products;

-- ALTER TABLE

ALTER TABLE products ADD COLUMN email VARCHAR(100);

ALTER TABLE products MODIFY COLUMN price INT;

ALTER TABLE products DROP COLUMN email;

ALTER TABLE products CHANGE COLUMN description descr VARCHAR(100);

ALTER TABLE products ADD CONSTRAINT unique_id UNIQUE(product_id);

-- Temporary Table
CREATE TEMPORARY TABLE temp_sales (
    sale_id INT,
    product_id INT,
    sale_amount DECIMAL(10, 2)
);

INSERT INTO temp_sales (sale_id, product_id, sale_amount) VALUES
(1, 101, 150.00),
(2, 102, 200.00),
(3, 101, 250.00),
(4, 103, 300.00);

SELECT * FROM temp_sales;

SELECT SUM(sale_amount) AS total_sales
FROM temp_sales;

CREATE TEMPORARY TABLE temp_products LIKE products;

SELECT * FROM temp_products;

DROP TEMPORARY TABLE IF EXISTS temp_sales;