import sqlite3


def main():
    conn = None
    try:
        conn = sqlite3.connect('Data/employees.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')

        cur.execute('''INSERT INTO Employees
                        (Name, Position, DepartmentID, LocationID)
                        VALUES
                        ('Ilya Yashin', 'Programming', 4, 4)''')
        conn.commit()
        print('Employee was successfully added.')

        cur.execute('''SELECT 
                        Employees.Name,
                        Departments.DepartmentName,
                        Locations.LocationName
                    FROM Employees, Departments, Locations
                    WHERE 
                        Employees.DepartmentID == Departments.DepartmentID AND
                        Employees.LocationID == Locations.LocationID''')
        result = cur.fetchall()
        for row in result:
            print(f'{row[0]:15} - {row[1]:25} - {row[2]}')
    except sqlite3.Error as err:
        print(err)
    finally:
        if conn != None:
            conn.close()


if __name__ == '__main__':
    main()