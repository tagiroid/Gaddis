import Employee

def main():
    emp_1 = Employee.employee('Susan meyers', '47899', 'Buch', 'VC')
    emp_2 = Employee.employee('Mark Jones', '39119', 'IT', 'Programming')
    emp_3 = Employee.employee('Joy Rodgers', '81774', 'Production', 'Engineer')

    print('Employee 1: ')
    display_emp(emp_1)
    print()

    print('Employee 2: ')
    display_emp(emp_2)
    print()

    print('Employee 3: ')
    display_emp(emp_3)
    print()

def display_emp(employee):
    print('Name: ', employee.get_name())
    print('ID: ', employee.get_id())
    print('Branch: ', employee.get_branch())
    print('Position: ', employee.get_position())

if __name__ == '__main__':
    main()