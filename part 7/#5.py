import os
found = False
search = input('Find the bill №: ')
file = open('charge_accounts.txt', 'r')
line = file.readline()

while line != '':
    line = line.rstrip('\n')
    if line == search:
        print('is in!')
        found = True
    line = file.readline()
if not found:
    print('is not')

file.close()