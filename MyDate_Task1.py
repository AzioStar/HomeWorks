import calendar

class MyDate:
    Months = ["","Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr",
            "Noyabr", "Dekabr"]
    
    Days_In_Months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self,day,month,year):
        self.__day = day
        self.__month = month
        self.__year = year

    @staticmethod
    def isLeapYear(year):
        if calendar.isleap(year):
            return f"Leap Year"
        else:
            return f"Not leap year"

    @staticmethod
    def isValidDate(day, month, year):
        if not (1 <= year <= 9999):
            raise ValueError("Please enter Valide date and try again")
        
        if not (1 <= month <= 12):
            raise ValueError("Please enter Valide date and try again")
    
        max_days = MyDate.Days_In_Months[month]
        if month == 2 and calendar.isleap(year):
            max_days = 29

        if not (1 <= day <= max_days):
            raise ValueError("Please enter Valide date and try again")
        
        return True

    def setDate(self, day, month, year):
        if not self.isValidDate(day, month, year):
            raise ValueError("Please enter Valide date and try again")
        self.__day = day
        self.__month = month
        self.__year = year
        

    def nextDay(self):
        max_days = MyDate.Days_In_Months[self.__month]
        if self.__month == 2 and calendar.isleap(self.__year):
            max_days = 29
        if self.__day < max_days:
            self.__day += 1
        else: 
            self.__day = 1
            if self.__month < 12:
                self.__month += 1
            else:
                self.__month = 1
                self.__year += 1
    
    def previousDay(self):
        if self.__day > 1:
            self.__day -= 1
        else:
            if self.__month > 1:
                self.__month -= 1
            else:
                self.__month = 12
                self.__year -= 1
        max_days = MyDate.Days_In_Months[self.__month]
        if self.__month == 2 and calendar.isleap(self.__year):
            max_days = 29
        self.__day = max_days

    def nextMonth(self):
        if self.__month < 12:
            self.__month += 1
        else:
            self.__month = 1
            self.__year += 1
        max_days = MyDate.Days_In_Months[self.__month]
        if self.__month == 2 and calendar.isleap(self.__year):
            max_days = 29
        self.__day = max_days

    def previousMonth(self):
        if self.__month > 1:
            self.__month -= 1
        else:
            self.__month = 12
            self.__year -= 1
        max_days = MyDate.Days_In_Months[self.__month]
        if self.__month == 2 and calendar.isleap(self.__year):
            max_days = 29
        self.__day = max_days

    def nextYear(self):
        self.__year += 1
        if self.__month == 2 and calendar.isleap(self.__year):
            self.__day = 29

    def previousYear(self):
        self.__year -= 1
        if self.__month == 2 and calendar.isleap(self.__year):
            self.__day = 29

    def __str__(self):
        return f"{self.__day}-{self.Months[self.__month]}-{self.__year}"
    

try:
    day = int(input("Please enter the day: "))    
    month = int(input("Pleaes enter the month: "))
    year = int(input("Pleaes enter the year: "))
    date = MyDate(day,month,year)
    result = date.isValidDate(day,month,year)
except:
    print("Please enter Valid value and try again!")

print(date)
