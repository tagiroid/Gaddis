def main():

    num1 = int(input('Enter integer: '))
    num2 = int(input('Enter another integer: '))

    print('The greatest common divisor is: ')
    print(gcd(num1, num2))
    
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x%y)

if __name__ == '__main__':
    main()