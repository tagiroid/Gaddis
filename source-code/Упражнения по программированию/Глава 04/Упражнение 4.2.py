# Упражнение по программированию 4.2

# Сожженные калории

# Объявить и инициализировать переменную
# для калорий, сжигаемых в минуту.
caloriesPerMinute = 4.2

# Объявить переменные для количества сожженных калорий и
# количества минут.
caloriesBurned = 0.0
minutes = 0

print ('Минуты\t\tСожженные калории')
print ('---------------------------------')

# Исполнить цикл for, чтобы показать сожженные калории.
for minutes in range(10, 31, 5):
    caloriesBurned = caloriesPerMinute * minutes
    print (minutes, "\t\t", caloriesBurned)