import accounts

def main():
    print('Enter data: ')
    account_number = input('Acc num:')
    int_rate = input('Rate: ')
    balance = input('Balance: ')

    savings = accounts.SavingAccount(account_number, int_rate, balance)

    print('Enter CD data: ')
    account_number = input('Acc num:')
    int_rate = input('Rate: ')
    balance = input('Balance: ')
    maturity = input('Maturity: ')

    cd = accounts.CD(account_number, int_rate, balance, maturity)

    print(f' Number: {savings.get_number()}')
    print(f' Percent rate: {savings.get_rate()}')
    print(f' Balance: ${savings.get_balance()}')
    print()
    print(f' Number: {cd.get_number()}')
    print(f' Percent rate: {cd.get_rate()}')
    print(f' Balance: ${cd.get_balance()}')
    print(f' Maturity: {cd.get_date()}')
if __name__ == '__main__':
    main()