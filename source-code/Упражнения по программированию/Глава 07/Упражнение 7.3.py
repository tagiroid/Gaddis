# Упражнение по программированию 7.3

# Статистика дождевых осадков

def main():
    
    # Локальные переменные
    total = 0.0
    average = 0.0
    highest = 0.0
    lowest = 0.0
    month_lowest = ''
    month_highest = ''

    # Список для данных о дождевых осадках
    month_rain = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    # Инициализировать список названиями месяцев.
    month_list = ['январь', 'февраль', 'март',
                  'апрель', 'май', 'июнь', 'июль',
                  'август', 'сентябрь', 'октябрь',
                  'ноябрь', 'декабрь']

    # Получить величину дождевых осадков за каждый месяц.
    for i in range(12):
        month_rain[i] = float(input('Введите дождевые осадки за ' \
                                    + month_list[i] + ": "))

    # Вычислить суммарную величину.
    total = sum(month_rain)
    
    # Вычислить среднюю величину.
    average = total / 12.0
    
    # Вычислить максимальную величину.
    highest = max(month_rain)

    # Получить индекс месяца с самой высокой величиной дождевых осадков.
    month_highest = month_rain.index(highest)

    # Вычислить минимум.
    lowest = min(month_rain)

    # Получить индекс месяца с самой низкой величиной дождевых осадков.
    month_lowest = month_rain.index(lowest) 

    # Показать результаты
    print('Суммарная величина дождевых осадков:', 
	      format(total, '.2f'))
    print('Средняя величина дождевых осадков:', 
	      format(average, '.2f'))
    print('Максимальная величина дождевых осадков:', 
	      month_list[month_highest])
    print('Минимальная величина дождевых осадков:', 
	      month_list[month_lowest])

# Вызвать главную функцию.
main()