def main():
    n = int(input('number of rows = '))
    stars(n)
def stars(n):
    if n > 0:
        stars(n - 1)
        print('*' * n)
if __name__ == '__main__':
    main()