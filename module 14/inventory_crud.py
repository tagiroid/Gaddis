import sqlite3

MIN = 1
MAX = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
QUIT = 5


def main():
    choice = 0
    while choice != QUIT:
        display_menu()
        choice = get_menu_choice()
        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()


def display_menu():
    print('--------Menu---------')
    print('1. Create.')
    print('2. Read.')
    print('3. Update.')
    print('4. Delete.')
    print('5. Quit.')


def get_menu_choice():
    choice = int(input('Choose your option: '))

    while choice < MIN or choice > MAX:
        print(f'Please choose option between {MIN} and {MAX}.')
        choice = int(input('Choose your option: '))

    return choice


def create():
    print('Create a new position.')
    name = input('The name of position: ')
    price = input('Price: ')
    insert_row(name, price)


def read():
    name = input('Search for position: ')
    num_found = display_item(name)
    print(f'{num_found} row(s) found.')


def update():
    read()
    selected_id = int(input('Choose position to update: '))
    name = input('Enter new name: ')
    price = input('Enter new price: ')
    num_updated = update_row(selected_id, name, price)
    print(f'{num_updated} row(s) updated.')


def delete():
    read()
    selected_id = int(input('Choose position to delete: '))
    sure = input('Are you sure you want to delete this position? y/n\n')
    if sure.lower() == 'y':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} row(s) deleted.')


def insert_row(name, price):
    conn = None
    try:
        conn = sqlite3.connect('Data/inventory.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                        VALUES (?,?)''',
                    (name, price))
        conn.commit()
    except sqlite3.Error as err:
        print('Database error', err)
    finally:
        if conn != None:
            conn.close()


def display_item(name):
    conn = None
    result = []
    try:
        conn = sqlite3.connect('Data/inventory.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Inventory
                    WHERE ItemName == ?''',
                    (name, ))
        result = cur.fetchall()
        for row in result:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15}'
                  f'Price:  {row[2]:<6}')
    except sqlite3.Error as err:
        print('Database error', err)
    finally:
        if conn != None:
            conn.close()
        return len(result)


def update_row(id, name, price):
    conn = None
    try:
        conn = sqlite3.connect('Data/inventory.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Inventory
                        SET ItemName == ?, Price ==?
                        WHERE ItemID == ?''',
                    (name, price, id))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Database error', err)
    finally:
        if conn != None:
            conn.close()
        return num_updated


def delete_row(id):
    conn = None
    try:
        conn = sqlite3.connect('Data/inventory.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Inventory
                        WHERE ItemID == ?''',
                    (id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Database error', err)
    finally:
        if conn != None:
            conn.close()
        return num_deleted


if __name__ == '__main__':
    main()