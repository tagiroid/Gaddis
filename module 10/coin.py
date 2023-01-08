import random

class Coin:

    def __init__(self):
        self.__sideup = 'heads'

    def toss(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'heads'
        else:
            self.__sideup = 'tales'

    def get_sideup(self):
        return self.__sideup

