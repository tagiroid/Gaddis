# Эта программа демонстрирует, как прочитанные из файла 
# числа конвертируются из строкового представления
# перед тем, как они используются в математической операции.

def main():
    # Открыть файл для чтения.
    infile = open('numbers.txt', 'r')

    # Прочитать три числа из файла.
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Закрыть файл.
    infile.close()

    # Сложить три числа.
    total = num1 + num2 + num3

    # Показать числа и их сумму.
    print('Числа: {num1}, {num2}, {num3}')
    print('Их сумма: {total}')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()