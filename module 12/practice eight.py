def main():
    n1 = ackermann(0,3)
    print(n1)
    n2 = ackermann(2,0)
    print(n2)
    n3 = ackermann(2,3)
    print(n3)
def ackermann(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
if __name__ == '__main__':
    main()