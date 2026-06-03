class Computer:
    def __init__(self):
        self.computer_name = ""
        self.RAM = 0
        self.price = 0
        self.processor = ""

    def adding(self):
        print("")
        self.computer_name = input("Computer nomini kiritin: ")
        self.RAM = int(input("RAM: "))
        self.price = float(input("Narxini kiriting: "))
        self.processor = input("Processor: ")

    def showing(self):
        print("")
        print(f"Computer nomi: {self.computer_name}")
        print(f"RAM: {self.RAM}")
        print(f"Narxi: {self.price}")
        print(f"Processor: {self.processor}")

lst = []
for i in range(4):
    a = Computer()
    a.adding()
    lst.append(a)

print("RAM 4 dan katta bolgan komputerlar bu 16 kichik: ")
for i in lst:
    if 4 <= i.RAM <= 16:
        i.showing()