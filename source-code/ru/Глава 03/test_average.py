# Эта программа получает три оценки за контрольные работы и
# показывает их средний балл. Она поздравляет пользователя, 
# если средний балл высокий.

# Именованная константа HIGH_SCORE содержит значение, которое
# считается высоким баллом.
HIGH_SCORE = 95
 
# Получить три оценки за тесты.
test1 = int(input('Введите оценку 1: ' ))
test2 = int(input('Введите оценку 2: ' ))
test3 = int(input('Введите оценку 3: ' ))

# Рассчитать средний балл.
average = (test1 + test2 + test3) / 3

# Напечатать средний балл.
print('Средний балл составляет:', average)

# Если средний балл высокий, то
# поздравить пользователя.
if average >= HIGH_SCORE:
    print('Поздравляем!')
    print('Отличный средний балл!')