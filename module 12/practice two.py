def main():
    x = int(input('x = '))
    y = int(input('y = '))

    print(x, 'multiplied by', y, 'is equal', multi(x, y))
def multi(x,y):
    if x == 0 or y == 0:
        return 0
    else:
        return x + multi(x, y - 1)
if __name__ == '__main__':
    main()