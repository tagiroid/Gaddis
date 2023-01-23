# Упражнение по программированию 12.8

# Функция Аккерманна

def main():
    # Тестовое значение 1
    num1 = ackermann(0, 3)
    print(num1)

    # Тестовое значение 2
    num2 = ackermann(2, 0)
    print(num2)

    # Тестовое значение 3
    num3 = ackermann(2, 3)
    print(num3)
    
# Функция Аккерманна является рекурсивным математическим алгоритмом,
# который используется для проверки, насколько успешно система 
# оптимизирует свою производительность в случае рекурсии.
def ackermann(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Вызвать главную функцию.
main()