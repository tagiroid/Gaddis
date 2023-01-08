import bankaccount

def main():
    start_bal = float(input('Enter your starting amount: '))

    savings = bankaccount.BankAccount(start_bal)

    pay = float(input('How much did you get this week?: '))
    print('Adding to your account...')
    savings.deposit(pay)

    print(f'It is left on your account $ {savings.get_balance():,.2f}.')

    cash = float(input('How much do you want to withdraw? '))
    print('Withdrawing...')
    savings.withdraw(cash)

    print(f'Amount left ${savings.get_balance():,.2f}.')

if __name__ == '__main__':
    main()