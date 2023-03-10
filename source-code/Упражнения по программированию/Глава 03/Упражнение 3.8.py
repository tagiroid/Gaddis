# Упражнение по программированию 3.8

# Калькулятор сосисок для пикника

# Глобальные переменные
HOT_DOGS_PER_PACKAGE = 10  # количество сосисок в упаковке
BUNS_PER_PACKAGE = 8       # количество булочек в упаковке

# Локальные переменные
numAttending = 0    # Количество участников пикника
numPerPerson = 0    # Количество сосисок и булочек в расчете на человека
total = 0           # Общее количество требующихся сосисок и булочек
minDogs = 0         # Минимальное количество упаковок сосисок
minBuns = 0         # TМинимальное количество упаковок булочек
dogsLeft = 0        # Количество сосисок, оставшихся в упаковке
bunsLeft = 0        # Количество булочек, оставшихся в упаковке

# Получить от пользователя количество людей, посещающих пикник.
numAttending = int(input('Введите количество людей, посещающих пикник: '))

# Получить от пользователя количество хот-догов в расчете на участника.
numPerPerson = int(input('Введите количество хот-догов в расчете на человека: '))

# Вычислить общее количество требующихся сосисок и булочек.
total = numAttending * numPerPerson

# Вычислить минимальное количество требующихся упаковок с сосисками.
minDogs = total // HOT_DOGS_PER_PACKAGE

# Определить, является ли количество посещающих людей
# достаточно большим, что требуется более одной упаковки
# сосисок.
if minDogs > 0:
    # Вычислить количество сосисок, оставшихся
    # в упаковке, если есть.
    dogsLeft = total % HOT_DOGS_PER_PACKAGE
    
    # Если будут остатки, то добавить дополнительную
    # упаковку сосисок.
    if dogsLeft != 0:
        minDogs += 1
            
# Количество посещающих людей достаточно малое, и поэтому
# требуется только одна упаковка сосисок.
else:
    # Присвоить минимальному количеству упаковок сосисок значение 1.
    minDogs = 1
        
# Определить количество оставшихся сосисок, если есть.
dogsLeft = HOT_DOGS_PER_PACKAGE * minDogs - total

# Вычислить минимальное количество упаковок булочек, 
# необходимых для хот-догов.
minBuns = total // BUNS_PER_PACKAGE

# Определить, является ли количество посещающих людей
# достаточно большим, что требуется более одной упаковки
# булочек для хот-догов.
if minBuns > 0:
    # Вычислить количество булочек для хот-догов, оставшихся
    # в упаковке, если есть.
    bunsLeft = total % BUNS_PER_PACKAGE
        
    # Если будут остатки, то добавить дополнительную
    # упаковку булочек для хот-догов.
    if bunsLeft != 0:
        minBuns += 1
            
# Количество посещающих людей достаточно малое, и поэтому
# требуется только одна упаковка булочек для хот-догов.            
else:
    # Присвоить минимальному количеству упаковок булочек 
    # для хот-догов значение 1.
    minBuns = 1

# Вычислить количество оставшихся булочек для хот-догов, если есть.
bunsLeft = BUNS_PER_PACKAGE * minBuns - total
    
# Показать минимальное количество требующихся упаковок сосисок.
print('Минимальное количество требующихся упаковок сосисок:', minDogs)

# Показать минимальное количество требующихся упаковок булочек.
print('Минимальное количество требующих упаковок булочек:', minBuns)

# Показать количество оставшихся сосисок.
print('Количество оставшихся сосисок:', dogsLeft)

# Показать количество оставшихся булочек для хот-догов.
print('Количество оставшихся булочек:', bunsLeft)