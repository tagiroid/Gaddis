import Information

def main():
    name = input('Name: ')
    address = input('Address: ')
    age = input('Age: ')
    phone = input('Phone: ')
    person_1 = Information.Information(name, address, age, phone)
    person_2 = Information.Information(name, address, age, phone)
    person_3 = Information.Information(name, address, age, phone)

    print('Info about me:')
    display_info(person_1)
    print()

    print('Info about him:')
    display_info(person_2)
    print()

    print('Info about her:')
    display_info(person_3)
    print()

def display_info(Information):
    print(' Имя:     ', Information.get_name())
    print(' Адрес:   ', Information.get_address())
    print(' Возраст: ', Information.get_age())
    print(' Телефон: ', Information.get_phone())

if __name__ == '__main__':
    main()