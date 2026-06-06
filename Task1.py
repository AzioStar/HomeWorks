from random import randint
class student:
    def __init__(self,name,stuent_id):
        self.name = name
        self.id = stuent_id
        self.grades = []

    def add_grade(self,grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_status(self):
        average = self.calculate_average()
        if 90 <= average <= 100:
            return f"A'lo"
        elif 80 <= average <= 89:
            return f"Yaxshi"
        elif 70 <= average <= 79:
            return f"Qoniqarli"
        else:
            return f"Qoniqarsiz"
    
a1 = student("Aiden","S100")
a2 = student("Simon","S101")
a3 = student("John","S102")
lst = [a1,a2,a3]

for i in lst:
    for x in range(3):
        i.add_grade(randint(50,100))

print(f"Name: {a1.name}, Average: {a1.calculate_average():.2f}, Status: {a1.get_status()}")
print(f"Name: {a2.name}, Average: {a2.calculate_average():.2f}, Status: {a2.get_status()}")
print(f"Name: {a3.name}, Average: {a3.calculate_average():.2f}, Status: {a3.get_status()}")