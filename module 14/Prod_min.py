import sqlite3


def main():
    # Minimal ordered prices
    conn = sqlite3.connect('Data/chocolate.db')
    cur = conn.cursor()

    min_price = float(input('Enter the minimal price: '))

    cur.execute('''SELECT Description, RetailPrice FROM Products
                    WHERE RetailPrice >=?
                    ORDER BY RetailPrice''', (min_price,))

    result = cur.fetchall()

    if len(result) > 0:
        print('Here is results:')
        print()
        print('Description                         Price')
        print('-----------------------------------------')

        for row in result:
            print(f'{row[0]:35} {row[1]:>5}')
    else:
        print('Nothing was found')

    cur.execute('SELECT MIN(RetailPrice) FROM Products')
    lowest = cur.fetchone()[0]
    cur.execute('SELECT MAX(RetailPrice) FROM Products')
    highest = cur.fetchone()[0]
    cur.execute('SELECT AVG(RetailPrice) FROM Products')
    average = cur.fetchone()[0]

    print(f'Minimal price: ${lowest:.2f}')
    print(f'Maximal price: ${highest:.2f}')
    print(f'Average price: ${average:.2f}')
    conn.close()


if __name__ == '__main__':
    main()
