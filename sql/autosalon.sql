CREATE DATABASE autosalon CHARACTER SET utf8mb4;
USE autosalon;

CREATE TABLE customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    active BOOLEAN NOT NULL
);

CREATE TABLE car (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    price FLOAT NOT NULL,
    fuel ENUM('petrol','diesel','electric') NOT NULL,
    available BOOLEAN NOT NULL
);

CREATE TABLE equipment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL
);

CREATE TABLE car_order (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    created_at DATETIME NOT NULL,
    status ENUM('new','paid','cancelled') NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

CREATE TABLE order_equipment (
    order_id INT NOT NULL,
    equipment_id INT NOT NULL,
    PRIMARY KEY (order_id, equipment_id),
    FOREIGN KEY (order_id) REFERENCES car_order(id),
    FOREIGN KEY (equipment_id) REFERENCES equipment(id)
);

CREATE TABLE payment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    amount FLOAT NOT NULL,
    paid BOOLEAN NOT NULL,
    FOREIGN KEY (order_id) REFERENCES car_order(id)
);

CREATE VIEW v_order_total AS
SELECT
    o.id AS order_id,
    c.name AS customer,
    car.brand,
    car.model,
    car.price + IFNULL(SUM(e.price), 0) AS total_price
FROM car_order o
JOIN customer c ON o.customer_id = c.id
JOIN car ON car.id = o.id
LEFT JOIN order_equipment oe ON o.id = oe.order_id
LEFT JOIN equipment e ON oe.equipment_id = e.id
GROUP BY o.id;

CREATE VIEW v_car_sales AS
SELECT
    brand,
    COUNT(*) AS sold
FROM car
JOIN car_order o ON car.id = o.id
GROUP BY brand;

INSERT INTO customer (name, email, active) VALUES
('Jan Novák', 'jan.novak@email.cz', TRUE),
('Petr Svoboda', 'petr.svoboda@email.cz', TRUE),

INSERT INTO car (brand, model, price, fuel, available) VALUES
('Škoda', 'Octavia', 520000, 'petrol', TRUE),
('Škoda', 'Superb', 780000, 'diesel', TRUE),

INSERT INTO equipment (name, price) VALUES
('Klimatizace', 25000),
('Vyhřívaná sedadla', 18000),

INSERT INTO car_order (customer_id, created_at, status) VALUES
(1, '2025-01-10 10:15:00', 'new'),
(2, '2025-01-11 11:30:00', 'paid'),

INSERT INTO order_equipment (order_id, equipment_id) VALUES
(1, 1),
(1, 2),

INSERT INTO payment (order_id, amount, paid) VALUES
(1, 545000, FALSE),
(2, 825000, TRUE),
