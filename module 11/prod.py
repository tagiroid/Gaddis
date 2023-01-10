class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name
    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number

class ProductionWorker(Employee):
    def __init__(self, name, number, shift, rate):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__rate = rate

    def set_shift(self,shift):
        self.__shift = shift
    def set_rate(self, rate):
        self.__rate = rate

    def get_shift(self):
        return self.__shift
    def get_rate(self):
        return self.__rate

class ShiftSupervisor(Employee):
    def __init__(self, name, salary, bonus):
        Employee.__init__(self, name, number)
        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary
    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary
    def get_bonus(self):
        return self.__bonus
