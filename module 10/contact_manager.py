import contact
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'

def main():
    mycontacts = load_contacts()

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    save_contacts(mycontacts)

def load_contacts():
    try:
        input_file = open(FILENAME, 'rb')
        contact_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        contact_dct = {}

    return contact_dct

def get_menu_choice():

    print()
    print('Menu')
    print('----')
    print('1. Look Up')
    print('2. Add')
    print('3. Change')
    print('4. Delete')
    print('5. Quit')
    print()

    choice = int(input('What you want to do?: '))

    while LOOK_UP > choice or choice > QUIT:
        choice = int(input('What you want to do?: '))

    return choice

def look_up(mycontacts):

    name = input('Enter name: ')

    print(mycontacts.get(name, 'This name wasnt found'))

def add(mycontacts):

    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')

    entry = contact.Contact(name, phone, email)

    if name not in mycontacts:
        mycontacts[name] = entry
        print('Name added')
    else:
        print('This name is already in')

def change(mycontacts):
    name = input('Enter the name: ')

    if name in mycontacts:
        phone = input('Enter new phone: ')
        email = input('Enter new Email: ')

        entry = contact.Contact(name, phone, email)

        mycontacts[name] = entry

        print('Data was changed')
    else:
        print('No such name')

def delete(mycontacts):
    name = input('Name: ')

    if name in mycontacts:
        del mycontacts[name]
        print('Name was deleted')
    else:
        print('No such name')

def save_contacts(mycontacts):
    output_file = open(FILENAME, 'wb')
    pickle.dump(mycontacts, output_file)
    output_file.close()
    
if __name__ == '__main__':
    main()