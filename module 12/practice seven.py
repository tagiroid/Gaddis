def main():
    digit = int(input('Enter digit: '))
    power = int(input('Enter power: '))
    print(f'Your answer is {pow(digit, power)}')

def pow(x,y):
    if y == 0:
        return 1
    else:
        return x * pow(x, y-1)
if __name__ == '__main__':
    main()