import pickle
import cellphone

FILENAME = 'cellphone.dat'

def main():

    end_of_file = False

    input_file = open(FILENAME, 'rb')

    while not end_of_file:
        try:
            phone = pickle.load(input_file)
            display_data(phone)
        except EOFError:
            end_of_file = True

    input_file.close()

def display_data(phone):
    print('Here is:')
    print(f'Manufacturer: {phone.get_manufact()}')
    print(f'Model: {phone.get_model()}')
    print(f'Price: {phone.get_retail_price():,.2f}')

if __name__ == '__main__':
    main()