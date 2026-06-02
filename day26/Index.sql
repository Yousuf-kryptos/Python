-- INDEXES
-- CREATE INDEX

CREATE INDEX product_index ON products (product);

SELECT * FROM products;

EXPLAIN SELECT * FROM products WHERE product = 'Laptop';

-- SHOW INDEX

SHOW INDEX FROM products;

SHOW INDEX FROM products FROM flaskdb;

SHOW INDEX FROM flaskdb.products;

-- DROP INDEX

DROP INDEX product_index ON products;