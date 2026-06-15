CREATE TABLE author(id int AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50));

CREATE TABLE genre(id int AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(50));

CREATE TABLE book(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2),
    amount INT,
    a_id INT,
    g_id INT,
    FOREIGN KEY (a_id) REFERENCES author(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (g_id) REFERENCES genre(id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO author(name) VALUES("George Orwell"),("Jane Austen"),("F. Scott Fitzgerald"),("J.R.R. Tolkien");
INSERT INTO genre(name) VALUES("Dystopian"),
                              ("Romance"),
                              ("High Fantasy"),
                              ("Literary Fiction"),
                              ("Political Satire"),
                              ("Mythology");


INSERT INTO book (name, price, amount, a_id, g_id) 
VALUES 
('1984', 15.99, 10, 1, 1),
('Animal Farm', 12.50, 15, 1, 5),
('Burmese Days', 18.00, 5, 1, 4),
('Pride and Prejudice', 10.99, 20, 2, 2),
('Sense and Sensibility', 11.50, 12, 2, 2),
('Emma', 13.00, 8, 2, 2),
('The Hobbit', 20.00, 25, 3, 3),
('The Fellowship of the Ring', 25.00, 15, 3, 3),
('The Silmarillion', 22.00, 7, 3, 6),
('The Great Gatsby', 14.00, 30, 4, 4),
('Tender Is the Night', 16.00, 6, 4, 4),
('The Beautiful and Damned', 15.00, 4, 4, 4);

SELECT * FROM book as b
    JOIN author as a
    ON b.a_id = a.id WHERE a.name="George Orwell";
+----+--------------+-------+--------+------+------+----+---------------+
| id | name         | price | amount | a_id | g_id | id | name          |
+----+--------------+-------+--------+------+------+----+---------------+
|  1 | 1984         | 15.99 |     10 |    1 |    1 |  1 | George Orwell |
|  2 | Animal Farm  | 12.50 |     15 |    1 |    5 |  1 | George Orwell |
|  3 | Burmese Days | 18.00 |      5 |    1 |    4 |  1 | George Orwell |
+----+--------------+-------+--------+------+------+----+---------------+

SELECT a.name, JSON_ARRAYAGG(g.name) as genres FROM book as b
    JOIN author as a ON b.a_id = a.id
    JOIN genre as g ON b.g_id = g.id
        GROUP BY a.name;
+---------------------+--------------------------------------------------------------+
| name                | genres                                                       |
+---------------------+--------------------------------------------------------------+
| F. Scott Fitzgerald | ["High Fantasy", "High Fantasy", "Mythology"]                |
| George Orwell       | ["Dystopian", "Political Satire", "Literary Fiction"]        |
| J.R.R. Tolkien      | ["Literary Fiction", "Literary Fiction", "Literary Fiction"] |
| Jane Austen         | ["Romance", "Romance", "Romance"]                            |
+---------------------+--------------------------------------------------------------+

SELECT a.name, g.name as genre, COUNT(g.name) as total FROM book as b
    JOIN author as a ON b.a_id = a.id 
    JOIN genre as g ON b.g_id = g.id 
        GROUP BY a.name, g.name;
+---------------------+--------------------------------------------------------------+-------+
| name                | genre                                                        | total |
+---------------------+--------------------------------------------------------------+-------+
| F. Scott Fitzgerald | ["High Fantasy", "High Fantasy"]                             |     2 |
| F. Scott Fitzgerald | ["Mythology"]                                                |     1 |
| George Orwell       | ["Dystopian"]                                                |     1 |
| George Orwell       | ["Literary Fiction"]                                         |     1 |
| George Orwell       | ["Political Satire"]                                         |     1 |
| J.R.R. Tolkien      | ["Literary Fiction", "Literary Fiction", "Literary Fiction"] |     3 |
| Jane Austen         | ["Romance", "Romance", "Romance"]                            |     3 |
+---------------------+--------------------------------------------------------------+-------+

SELECT g.name, COUNT(g.name) as most FROM book as b
    JOIN genre as g ON b.g_id = g.id 
    GROUP BY g.name 
    ORDER BY most DESC LIMIT 1;
+------------------+------+
| name             | most |
+------------------+------+
| Literary Fiction |    4 |
+------------------+------+

SELECT a.name, g.name, COUNT(g.name) as most FROM book as b
    JOIN genre as g ON b.g_id = g.id 
    JOIN author as a ON b.a_id = a.id 
    GROUP BY a.name, g.name 
    ORDER BY most DESC;
+---------------------+------------------+------+
| name                | name             | most |
+---------------------+------------------+------+
| Jane Austen         | Romance          |    3 |
| J.R.R. Tolkien      | Literary Fiction |    3 |
| F. Scott Fitzgerald | High Fantasy     |    2 |
| George Orwell       | Dystopian        |    1 |
| George Orwell       | Political Satire |    1 |
| George Orwell       | Literary Fiction |    1 |
| F. Scott Fitzgerald | Mythology        |    1 |
+---------------------+------------------+------+

SELECT a.name, SUM(amount * price) AS total_books
FROM author AS a
JOIN book AS b ON a.id = b.a_id
GROUP BY a.name
ORDER BY total_books DESC LIMIT 1;
+---------------------+-------------+
| name                | total_books |
+---------------------+-------------+
| F. Scott Fitzgerald |     1029.00 |
+---------------------+-------------+

