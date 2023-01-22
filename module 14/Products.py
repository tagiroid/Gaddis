import sqlite3

def main():
    conn = sqlite3.connect('Data/chocolate.db')
    cur = conn.cursor()
    # Fetch all method
    print('Fetchall method:')
    cur.execute('SELECT Description, RetailPrice FROM Products')
    results = cur.fetchall()
    for rows in results:
        print(f'{rows[0]:35} - {rows[1]:5}')
    print()

    #fetch one method
    print('Fetchone method:')
    cur.execute('SELECT Description, RetailPrice FROM Products')
    row = cur.fetchone()
    while row != None:
        print(f'{row[0]:35} / {row[1]:5}')
        row = cur.fetchone()
    print()

    #Select all table at once
    print('"SELECT *" method:')
    cur.execute('SELECT * FROM Products')
    fetch = cur.fetchall()
    for r in fetch:
        print(f'{r[0]:2} - {r[1]:35} - {r[2]:5} - {r[3]:6} - {r[4]:5}')

    conn.close()

if __name__ == '__main__':
    main()