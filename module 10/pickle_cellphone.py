import pickle
import cellphone

FILENAME = 'cellphone.dat'

def main():

    again = 'y'

    output_file = open(FILENAME, 'wb')

    while again.lower() == 'y':
        man = input('manufacturer: ')
        mod = input('model: ')
        retail = float(input('price: '))

        phone = cellphone.CellPhone(man, mod, retail)

        pickle.dump(phone, output_file)

        again = input('Once again?: ')

    output_file.close()
    print(f'All data is saved into {FILENAME}')

if __name__ == '__main__':
    main()