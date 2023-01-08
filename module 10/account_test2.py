import bankaccount2

def main():
    start_bal = float(input('Enter your starting amount: '))

    savings = bankaccount2.BankAccount(start_bal)

    pay = float(input('How much did you get this week?: '))
    print('Adding to your account...')
    savings.deposit(pay)

    print(savings)

    cash = float(input('How much do you want to withdraw? '))
    print('Withdrawing...')
    savings.withdraw(cash)

    print(savings)

if __name__ == '__main__':
    main()