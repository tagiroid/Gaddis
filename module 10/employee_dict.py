import Employee

def main():

    name = input('Name: ')
    id = input('ID: ')
    branch = input('Branch: ')
    position = input('Position: ')
    employee = Employee.employee(name, id, branch, position)

    
if __name__ == '__main__':
    main()