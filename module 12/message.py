def main():
    message(5)

def message(times):
    if times > 0:
        print('This is recursion')
        message(times - 1)

if __name__ == '__main__':
    main()