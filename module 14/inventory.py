import sqlite3


def main():
    conn = sqlite3.connect('Data/inventory.db')
    cur = conn.cursor()

    cur.execute('''SELECT * FROM Inventory''')
    result = cur.fetchall()

    conn.close()

    for row in result:
        print(f'{row[0]:1} - {row[1]:12} - {row[2]:5} ')

    again = 'y'

    while again == 'y':
        id = int(input('ID: '))
        name = input('Name: ')
        price = float(input('Price: '))

        add_item(id, name, price)

        again = input('Again? y/n \n')


def add_item(id, name, price):
    conn = None

    try:
        conn = sqlite3.connect('Data/inventory.db')
        cur = conn.cursor()

        cur.execute('''INSERT INTO Inventory (ItemID, ItemName, Price)
                        VALUES (?,?,?)''',
                    (id, name, price))
        conn.commit()

    except sqlite3.Error as err:
        print(err)

    finally:
        if conn != None:
            conn.close()


if __name__ == '__main__':
    main()
