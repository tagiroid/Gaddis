import cellphone

def main():
    man = input('manufacturer: ')
    mod = input('model: ')
    retail = float(input('price: '))

    phone = cellphone.CellPhone(man, mod, retail)

    print('Here is:')
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model: {phone.get_model()}')
    print(f'Price: {phone.get_retail_price():,.2f}')
if __name__ == '__main__':
    main()