# Эта программа применяет рекурсию для нахождения
# наибольшего общего делителя (НОД или GCD) двух чисел.

def main():
    # Получить два числа.
    num1 = int(input('Введите целое число: '))
    num2 = int(input('Введите еще одно целое число: '))

    # Показать НОД (GCD).
    print(f'Наибольший общий делитель '
          f'этих двух чисел равен {gcd(num1, num2)}.')

# Функция gcd возвращает наибольший общий 
# делитель двух чисел.
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)

# Вызвать главную функцию.
if __name__ == '__main__':
    main()