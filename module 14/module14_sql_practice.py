import sqlite3


def main():
    conn = sqlite3.connect('Data/Inventory.db')
    cur = conn.cursor()
    #  creation
    cur.execute('''CREATE TABLE Inventory (ItemId INTEGER PRIMARY KEY NOT NULL,
                                            ItemName TEXT,
                                            Price REAL)''')
    # inserting
    again = 'y'

    while again == 'y':
        item_name = input('Name: ')
        price = float(input('Price: '))
        cur.execute('''INSERT INTO Inventory (ItemName, Price)
                        VALUES (?, ?)''', (item_name, price))

        again = input('One more position? y/n \n')
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()