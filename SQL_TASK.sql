CREATE TABLE computers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(50),
    cpu VARCHAR(50),
    frequency DECIMAL(3,1),
    ram INT,
    os VARCHAR(50),
    price DECIMAL(10,2));

INSERT INTO computers (brand, model, cpu, frequency, ram, os, price) VALUES
('Apple', 'MacBook Pro', 'Apple M1', 3.2, 16, 'macOS', 2500),
('Apple', 'MacBook Air', 'Apple M1', 3.0, 8, 'macOS', 900),
('Apple', 'iMac', 'Intel Core i7', 3.6, 16, 'macOS', 1800),
('ASUS', 'ZenBook', 'Intel Core i7', 3.9, 16, 'Windows 11', 1500),
('ASUS', 'Vivobook', 'Intel Core i5', 2.5, 8, 'Windows 10', 600),
('ASUS', 'ROG Zephyrus', 'AMD Ryzen 9', 4.8, 32, 'Windows 11', 2800),
('ASUS', 'ExpertBook', 'Intel Core i5', 2.4, 16, 'Windows 10', 1100),
('Dell', 'XPS 13', 'Intel Core i7', 3.8, 16, 'Windows 11', 1700),
('Dell', 'Inspiron', 'Intel Core i3', 2.1, 4, 'Windows 10', 450),
('Dell', 'Latitude', 'AMD Ryzen 5', 2.5, 8, 'Ubuntu 20.04', 800),
('HP', 'Spectre', 'Intel Core i7', 3.7, 16, 'Windows 11', 1600),
('HP', 'Pavilion', 'AMD Ryzen 5', 2.6, 8, 'Windows 10', 700),
('HP', 'EliteBook', 'Intel Core i5', 2.8, 8, 'Windows 10', 950),
('Lenovo', 'ThinkPad', 'Intel Core i7', 3.5, 16, 'Windows 11', 1400),
('Lenovo', 'IdeaPad', 'AMD Ryzen 3', 2.0, 4, 'Windows 10', 420),
('Lenovo', 'Yoga', 'Intel Core i5', 2.7, 8, 'Windows 11', 1100),
('Apple', 'Mac Mini', 'Intel Core i5', 2.6, 8, 'macOS', 700),
('ASUS', 'TUF Gaming', 'AMD Ryzen 7', 4.2, 16, 'Windows 11', 1300),
('Dell', 'Precision', 'Intel Core i9', 5.0, 32, 'Windows 11', 3000),
('HP', 'ProBook', 'AMD Ryzen 5', 2.5, 8, 'Ubuntu 22.04', 850);

mysql> SELECT * FROM computers ORDER BY price DESC LIMIT 1;
+----+-------+-----------+---------------+-----------+------+------------+---------+
| id | brand | model     | cpu           | frequency | ram  | os         | price   |
+----+-------+-----------+---------------+-----------+------+------------+---------+
| 19 | Dell  | Precision | Intel Core i9 |       5.0 |   32 | Windows 11 | 3000.00 |
+----+-------+-----------+---------------+-----------+------+------------+---------+

mysql> SELECT * FROM computers ORDER BY price ASC LIMIT 1;
+----+--------+---------+-------------+-----------+------+------------+--------+
| id | brand  | model   | cpu         | frequency | ram  | os         | price  |
+----+--------+---------+-------------+-----------+------+------------+--------+
| 15 | Lenovo | IdeaPad | AMD Ryzen 3 |       2.0 |    4 | Windows 10 | 420.00 |
+----+--------+---------+-------------+-----------+------+------------+--------+

SELECT frequency FROM computers WHERE price BETWEEN 400 AND 1000 AND cpu LIKE '%Intel%';
+-----------+
| frequency |
+-----------+
|       2.5 |
|       2.1 |
|       2.8 |
|       2.6 |
+-----------+

SELECT COUNT(*) FROM computers WHERE brand = 'Apple';
+----------+
| COUNT(*) |
+----------+
|        4 |
+----------+

SELECT * FROM computers WHERE os LIKE '%Windows%' AND ram > 8 AND brand = 'ASUS' ORDER BY price ASC;
+----+-------+--------------+---------------+-----------+------+------------+---------+
| id | brand | model        | cpu           | frequency | ram  | os         | price   |
+----+-------+--------------+---------------+-----------+------+------------+---------+
|  7 | ASUS  | ExpertBook   | Intel Core i5 |       2.4 |   16 | Windows 10 | 1100.00 |
| 18 | ASUS  | TUF Gaming   | AMD Ryzen 7   |       4.2 |   16 | Windows 11 | 1300.00 |
|  4 | ASUS  | ZenBook      | Intel Core i7 |       3.9 |   16 | Windows 11 | 1500.00 |
|  6 | ASUS  | ROG Zephyrus | AMD Ryzen 9   |       4.8 |   32 | Windows 11 | 2800.00 |
+----+-------+--------------+---------------+-----------+------+------------+---------+