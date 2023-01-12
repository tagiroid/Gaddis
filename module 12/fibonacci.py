def main():
    n = int(input('Enter number: '))

    print(f'The sum of {n}:')
    for numbers in range(1, n + 1):
        print(fib(numbers))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    main()