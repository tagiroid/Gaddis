class SavingAccount:

    def __init__(self, number, rate, balance):
        self.__number = number
        self.__rate = rate
        self.__balance = balance

    def set_number(self, number):
        self.__number = number
    def set_rate(self, rate):
        self.__rate = rate
    def set_balance(self, balance):
        self.__balance = balance

    def get_number(self):
        return self.__number
    def get_rate(self):
        return self.__rate
    def get_balance(self):
        return self.__balance

class CD(SavingAccount):

    def __init__(self, number, rate, balance, date):
        SavingAccount.__init__(self, number, rate, balance)
        self.__date = date

    def set_date(self, date):
        self.__date = date
    def get_date(self):
        return self.__date