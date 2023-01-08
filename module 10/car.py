class Car:

    def __init__(self, maker, model, year):
        self.__maker = maker
        self.__model = model
        self.__year = year

    def set_maker(self,maker):
        self.__maker = maker

    def set_model(self, model):
        self.__model = model

    def set_year(self,year):
        self.__year = year

    def get_maker(self):
        return self.__maker

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year