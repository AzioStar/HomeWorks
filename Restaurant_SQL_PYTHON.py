import pymysql

class Restaurant:
    def __init__(self):
        self.ConnectDB()
        self.CreateTB()

    def ConnectDB(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="group202"
        )
        self.c = self.db.cursor()

    def CreateTB(self):
        self.c.execute('''USE group202''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS Restaurant(id INT AUTO_INCREMENT PRIMARY KEY,
                                                                name VARCHAR(50) NOT NULL,
                                                                address VARCHAR(50) NOT NULL,
                                                                maxFoodPrice INT NOT NULL,
                                                                minFoodPrice INT NOT NULL,
                                                                employeesCount INT NOT NULL,
                                                                experience INT NOT NULL)''')

    def InsertDB(self):
        self.c.execute('''INSERT INTO Restaurant(name,address,maxFoodPrice,minFoodPrice,employeesCount,experience)
                                                VALUES("Golden Steakhouse", "Tashkent, Amir Temur St", 150, 40, 25, 15),
                                                      ("Burger King", "Tashkent, Navoi St", 12, 3, 15, 2),
                                                      ("Sushi Zen", "Samarkand, Registan Square", 80, 20, 10, 8),
                                                      ("Pasta Paradise", "Bukhara, Old City", 35, 10, 8, 5),
                                                      ("The Coffee Bean", "Tashkent, Yunusabad", 15, 2, 6, 3),
                                                      ("Ocean Seafood", "Tashkent, Chilanzar", 200, 60, 30, 20),
                                                      ("Taco Fiesta", "New York, Broadway", 25, 5, 12, 4),
                                                      ("Vegan Garden", "Berlin, Mitte", 45, 12, 7, 6),
                                                      ("Pizza Hut", "Tashkent, Tashkent City", 30, 7, 20, 10),
                                                      ("Dessert Heaven", "Namangan, Central Park", 20, 4, 5, 7)''')
        self.db.commit()
        
    def Letters(self):
        self.c.execute('''SELECT * FROM restaurant WHERE name LIKE "b%g"''')
        return self.c.fetchall()
    
    def LowPrice(self):
        self.c.execute('''SELECT name, minFoodPrice FROM restaurant GROUP BY name, minFoodPrice ORDER BY minFoodPrice LIMIT 3''')
        return self.c.fetchall()
    
    def MaxPrice(self):
        self.c.execute('''SELECT name, maxFoodPrice FROM restaurant ORDER BY maxFoodPrice DESC, experience DESC LIMIT 4''')
        return self.c.fetchall()

p = Restaurant()
# p.InsertDB()
for i in p.MaxPrice():
    print(i)