import prod

def main():
    name = input('Enter name: ')
    number = input('Enter ID: ')
    shift = int(input('Enter shift(1/2): '))
    rate = float(input('Enter rate: '))

    employee = prod.ProductionWorker(name, number, shift, rate)

    print('Your employee:')
    print('Name:', employee.get_name())
    print('ID:', employee.get_number())
    print('Shift:', employee.get_shift())
    print('Rate:', employee.get_rate())

if __name__ == '__main__':
    main()