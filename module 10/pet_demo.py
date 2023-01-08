import pet

def main():

    name = input("Enter the name: ")
    type = input("Enter the type: ")
    age = input("Enter age: ")

    my_pet = pet.Pet(name, type, age)

    print("Your pets name:", my_pet.get_name())
    print("Your pets type:", my_pet.get_animal_type())
    print("Your pets name:", my_pet.get_age())

if __name__ == '__main__':
    main()