import sqlite3


def main():
    conn = sqlite3.connect('Data/chocolate.db')
    cur = conn.cursor()

    pid = int(input('Enter product ID: '))

    cur.execute('''SELECT Description, RetailPrice FROM Products
                    WHERE ProductID == ?''', (pid,))
    results = cur.fetchone()

    if results != None:
        print(f'The current price for "{results[0]}" is: '
              f'${results[1]:.2f}')

        new_price = float(input('Enter the new price: '))

        cur.execute('''UPDATE Products
                    SET RetailPrice = ?
                    WHERE ProductID == ?''',
                    (new_price, pid))

        conn.commit()
        print('The price was changed.')
    else:
        print(f'The "{pid}" ID wasnt found.')

    print(cur.rowcount)
    conn.close()


if __name__ == '__main__':
    main()
