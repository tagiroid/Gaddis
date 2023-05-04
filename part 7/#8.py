# Это пограмма из 7 части, номер 8 Dylan Chloe

import os

def main():
    total =[]
    search = str(input("Search for name(s): ")).lower().split()

    print(search)
    boys = get_boys()
    girls = get_girls()
    names = boys + girls
    print(names)
    print(len(names))

    print(f'Name {search} is yes' if search in (boys or girls) else 'No')

    if len(search) > 1:
        for i in range(2):
            if search[i] in names:
                total.append(search[i])
        print(f'{str(total).split()} in top names' if len(total) > 0 else 'None')

def get_boys():
    boys_names = []
    file = open('BoyNames.txt', 'r')
    for line in file:
        name = str(line.rstrip('\n'))
        boys_names.append(name.lower())
    return boys_names

def get_girls():
    girls_names = []
    file = open('GirlNames.txt', 'r')
    for line in file:
        name = str(line.rstrip('\n'))
        girls_names.append(name.lower())
    return girls_names

if __name__ == '__main__':
    main()
