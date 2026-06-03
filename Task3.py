class User:
    def __init__(self, ism, surname, email):
        self.ism = ism
        self.surname = surname
        self.email = email

    def get_info(self):
        print("")
        print(f"Familiyasi: {self.surname}")
        print(f"Ismi: {self.ism}")
        print(f"Email: {self.email}")

a1 = User("Aiden", "Foster", "aiden@gmail.com")
a2 = User("Danny", "Thomas", "danny@gmail.com")
a3 = User("Simon", "Smith", "simon@gmail.com")

lst = [a1,a2,a3]
for i in lst:
    i.get_info()