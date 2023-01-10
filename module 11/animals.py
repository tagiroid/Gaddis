class Mammal:

    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print('I,m ', self.__species)
    def make_sound(self):
        print('Rrrrr!')

class Dog(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Dog')
    def make_sound(self):
        print('Wuf-wuf!')

class Cat(Mammal):
    def __init__(self):
        Mammal.__init__(self, 'Cat')
    def make_sound(self):
        print('Meow!')