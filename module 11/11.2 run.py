import prod

def main():
    name = input('Enter name: ')
    number = input('Enter ID: ')
    salary = int(input('Enter salary: '))
    bonus = float(input('Enter bonus: '))

    super = prod.ShiftSupervisor(name, number, salary, bonus)

    print('Your employee:')
    print('Name:', super.get_name())
    print('ID:', super.get_number())
    print('Shift:', super.get_salary())
    print('Rate:', super.get_bonus())
if __name__ == '__main__':
    main()