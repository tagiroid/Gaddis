import animals

def main():
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()

    print('Here are some animals and')
    print('sounds they make:')
    print('------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)

def show_mammal_info(creatute):
    creatute.show_species()
    creatute.make_sound()
if __name__ == '__main__':
    main()