-- CREATE DATABASE flaskdb; -- To create the database

-- USE flaskdb; -- to use the database

-- SHOW DATABASES; -- To show all the available databases

-- DROP DATABASE flaskdb; -- To drop the specified database

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10 , 2 ),
    description TEXT,
    order_date DATE,
    order_time TIME,
    coordinates POINT,
    quantity INT
);

DESCRIBE products;