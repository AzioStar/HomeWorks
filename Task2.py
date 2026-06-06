from random import randint
class employee:
    def __init__(self,name,emmpleyee_id,hourly_rate = 15.0):
        self.name = name
        self.id = emmpleyee_id
        self.hourly_rate = hourly_rate
        self.__working_hours = []

    def log_hours(self,hour):
        if 0 <= hour <= 24:
            self.__working_hours.append(hour)
            return True
        return False

    def total_hours(self):
        total = sum(self.__working_hours)
        return total

    def calculate_salary(self):
        salary = self.total_hours()
        return salary * self.hourly_rate

    def reset_hours(self):
        self.__working_hours.clear()
        if not self.__working_hours:
            return 0

a1 = employee("Aiden","S100")
a2 = employee("Simon","S101")
a3 = employee("John","S102")
lst = [a1,a2,a3]

for i in lst:
    for x in range(4):
        result = i.log_hours(randint(0,30))
        print(result)
    print(f"{i.name}, Total hours: {i.total_hours()}, Salary: {i.calculate_salary():.2f}, New week: {i.reset_hours()}")
