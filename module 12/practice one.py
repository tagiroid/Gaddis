def main():
    n = int(input('Enter number: '))
    recurs(n)


def recurs(n):
    if n > 1:
        recurs(n - 1)
    print(n)
if __name__ =='__main__':
    main()