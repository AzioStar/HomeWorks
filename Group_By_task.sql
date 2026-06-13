CREATE TABLE sales (
    id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price INT,
    quantity INT,
    sale_date DATE
);

INSERT INTO sales VALUES (1, 'Laptop', 'Electronics', 800, 2, '2025-01-01');
INSERT INTO sales VALUES (2, 'Phone', 'Electronics', 600, 3, '2025-01-01');
INSERT INTO sales VALUES (3, 'TV', 'Electronics', 900, 1, '2025-01-02');
INSERT INTO sales VALUES (4, 'Headphones', 'Electronics', 150, 5, '2025-01-03');

INSERT INTO sales VALUES (5, 'Table', 'Furniture', 300, 1, '2025-01-01');
INSERT INTO sales VALUES (6, 'Chair', 'Furniture', 100, 4, '2025-01-02');
INSERT INTO sales VALUES (7, 'Sofa', 'Furniture', 1200, 1, '2025-01-03');
INSERT INTO sales VALUES (8, 'Bed', 'Furniture', 900, 1, '2025-01-04');

INSERT INTO sales VALUES (9, 'T-shirt', 'Clothing', 40, 6, '2025-01-01');
INSERT INTO sales VALUES (10, 'Jeans', 'Clothing', 70, 3, '2025-01-02');
INSERT INTO sales VALUES (11, 'Jacket', 'Clothing', 120, 2, '2025-01-03');
INSERT INTO sales VALUES (12, 'Shoes', 'Clothing', 90, 4, '2025-01-04');

INSERT INTO sales VALUES (13, 'Apple', 'Food', 2, 20, '2025-01-01');
INSERT INTO sales VALUES (14, 'Bread', 'Food', 3, 15, '2025-01-02');
INSERT INTO sales VALUES (15, 'Milk', 'Food', 4, 10, '2025-01-03');
INSERT INTO sales VALUES (16, 'Cheese', 'Food', 8, 5, '2025-01-04');

INSERT INTO sales VALUES (17, 'Notebook', 'Stationery', 5, 10, '2025-01-01');
INSERT INTO sales VALUES (18, 'Pen', 'Stationery', 2, 25, '2025-01-02');
INSERT INTO sales VALUES (19, 'Marker', 'Stationery', 4, 12, '2025-01-03');
INSERT INTO sales VALUES (20, 'Folder', 'Stationery', 6, 8, '2025-01-04');


 select * from sales;
+----+--------------+-------------+-------+----------+------------+
| id | product_name | category    | price | quantity | sale_date  |
+----+--------------+-------------+-------+----------+------------+
|  1 | Laptop       | Electronics |   800 |        2 | 2025-01-01 |
|  2 | Phone        | Electronics |   600 |        3 | 2025-01-01 |
|  3 | TV           | Electronics |   900 |        1 | 2025-01-02 |
|  4 | Headphones   | Electronics |   150 |        5 | 2025-01-03 |
|  5 | Table        | Furniture   |   300 |        1 | 2025-01-01 |
|  6 | Chair        | Furniture   |   100 |        4 | 2025-01-02 |
|  7 | Sofa         | Furniture   |  1200 |        1 | 2025-01-03 |
|  8 | Bed          | Furniture   |   900 |        1 | 2025-01-04 |
|  9 | T-shirt      | Clothing    |    40 |        6 | 2025-01-01 |
| 10 | Jeans        | Clothing    |    70 |        3 | 2025-01-02 |
| 11 | Jacket       | Clothing    |   120 |        2 | 2025-01-03 |
| 12 | Shoes        | Clothing    |    90 |        4 | 2025-01-04 |
| 13 | Apple        | Food        |     2 |       20 | 2025-01-01 |
| 14 | Bread        | Food        |     3 |       15 | 2025-01-02 |
| 15 | Milk         | Food        |     4 |       10 | 2025-01-03 |
| 16 | Cheese       | Food        |     8 |        5 | 2025-01-04 |
| 17 | Notebook     | Stationery  |     5 |       10 | 2025-01-01 |
| 18 | Pen          | Stationery  |     2 |       25 | 2025-01-02 |
| 19 | Marker       | Stationery  |     4 |       12 | 2025-01-03 |
| 20 | Folder       | Stationery  |     6 |        8 | 2025-01-04 |
+----+--------------+-------------+-------+----------+------------+


SELECT category, SUM(quantity) as total from sales GROUP BY category;
+-------------+-------+
| category    | total |
+-------------+-------+
| Electronics |    11 |
| Furniture   |     7 |
| Clothing    |    15 |
| Food        |    50 |
| Stationery  |    55 |
+-------------+-------+

SELECT category, SUM(price) as total_sale from sales GROUP BY category;
+-------------+------------+
| category    | total_sale |
+-------------+------------+
| Electronics |       2450 |
| Furniture   |       2500 |
| Clothing    |        320 |
| Food        |         17 |
| Stationery  |         17 |
+-------------+------------+

SELECT category, AVG(price) as total_sale from sales GROUP BY category;
SELECT category, AVG(price) as total_sale from sales GROUP BY category;
+-------------+------------+
| category    | total_sale |
+-------------+------------+
| Electronics |   612.5000 |
| Furniture   |   625.0000 |
| Clothing    |    80.0000 |
| Food        |     4.2500 |
| Stationery  |     4.2500 |
+-------------+------------+

SELECT day(sale_date), SUM(price) as total_sale from sales GROUP BY day(sale_date);
+----------------+------------+
| day(sale_date) | total_sale |
+----------------+------------+
|              1 |       1747 |
|              2 |       1075 |
|              3 |       1478 |
|              4 |       1004 |
+----------------+------------+

SELECT category, SUM(price) as total_sale from sales where category="Electronics";
+-------------+------------+
| category    | total_sale |
+-------------+------------+
| Electronics |       2450 |
+-------------+------------+

SELECT category, SUM(price) as total_sale from sales GROUP BY category having total_sale > 2000;
+-------------+------------+
| category    | total_sale |
+-------------+------------+
| Electronics |       2450 |
| Furniture   |       2500 |
+-------------+------------+

SELECT category from sales GROUP BY category having AVG(price) > 100;
+-------------+
| category    |
+-------------+
| Electronics |
| Furniture   |
+-------------+

SELECT sale_date, SUM(quantity) from sales where sale_date="2025-01-01" GROUP BY sale_date;
+------------+---------------+
| sale_date  | SUM(quantity) |
+------------+---------------+
| 2025-01-01 |            42 |
+------------+---------------+

SELECT category from sales GROUP BY category ORDER BY SUM(quantity) DESC LIMIT 1;
+------------+
| category   |
+------------+
| Stationery |
+------------+

SELECT category, SUM(price*quantity) as total_sale from sales where quantity > 3 GROUP BY category;
+-------------+------------+
| category    | total_sale |
+-------------+------------+
| Electronics |        750 |
| Furniture   |        400 |
| Clothing    |        600 |
| Food        |        165 |
| Stationery  |        196 |
+-------------+------------+