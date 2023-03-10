# Упражнение по программированию 5.3

# Какова стоимость страховки?

# Глобальная константа для стоимости замещения в процентах
REPLACE_PERCENT = 0.8

# Главная функция
def main():
    # Локальные переменные
    replace= 0.0
    minInsure = 0.0

    # Получить стоимость замещения.
    replace = float(input('Введите стоимость замещения: '))

    # Вычислить сумму страховки
    minInsure = replace * REPLACE_PERCENT

    # Напечатать информацию о страховке.
    showInsure(replace, minInsure)
      
# Функция showInsure принимает в качестве аргументов значение  
# замещения replace и минимальной рекомендуемой страховки minInsure 
# и показывает информацию о сделке.
def showInsure (replace, minInsure):
    print (f'Стоимость замещения:\t${replace:,.2f}')
    print (f'Страхуемый процент:\t\t{int(REPLACE_PERCENT * 100)}%')
    print (f'Минимальная сумма, подлежащая страхованию: ${minInsure:,.2f}')

# Вызвать главную функцию.
main()