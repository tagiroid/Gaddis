def main():
    n = int(input('Enter number: '))
    fact = factorial(n)
    print(f'Factorial of {n} is {fact}')

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == '__main__':
    main()