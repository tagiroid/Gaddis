def main():
    n = int(input('Enter the number: '))
    print(f'The sum of numbers from 1 to {n} is {sum_of_all(n)}')

def sum_of_all(n):
    return n if n == 0 else n + sum_of_all(n-1)

if __name__ == '__main__':
    main()