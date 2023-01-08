import cellphone

def main():
    phones = make_list()

    print('Here is your data: ')
    display_list(phones)

def make_list():
    phone_list = []

    print('Enter 5 phones: ')

    for count in range(1,6):
        print('Number of phone' + str(count) + ':')
        man = input('manufacturer: ')
        mod = input('model: ')
        retail = float(input('price: '))
        print()

        phone = cellphone.CellPhone(man, mod,retail)
        phone_list.append(phone)
    return phone_list

def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()

if __name__ == '__main__':
    main()