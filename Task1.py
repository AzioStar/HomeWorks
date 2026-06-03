class Kitob:
    def __init__(self):
        self.book_name = ""
        self.author = ""
        self.price = 0
        self.owner = ""

    def adding(self):
        print("")
        self.book_name = input("Kitob nomini kiritin: ")
        self.author = input("Muallifni kiriting: ")
        self.price = float(input("Narxini kiriting: "))
        self.owner = input("Nashriyotni kiriting: ")

    def showing(self):
        print("")
        print(f"Kitob nomi: {self.book_name}")
        print(f"Muallifi: {self.author}")
        print(f"Narxi: {self.price}")
        print(f"Nashriyot: {self.owner}")

lst = []
for i in range(5):
    a = Kitob()
    a.adding()
    lst.append(a)

for i in lst:
    if "A" <= i.owner[0].upper() <= "H":
        i.showing()