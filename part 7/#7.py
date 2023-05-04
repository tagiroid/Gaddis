# Это программа для сдачи на водительские права

import os

def main():

    print('Это программа для сдачи на водительские права')
    print()

    get_your_answers()
    list_1 = get_true()
    list_2 = get_answers()
    count_results(list_1, list_2)

def get_your_answers():

    # создаем файл с ответами
    i_file = open('Your answers.txt', 'w')

    # и пустой список для него
    list = []

    # вписываем в него все наши ответы

    for num in range(20):
        list.append(str(input(f'Enter your answer for question #{num + 1}: ')))
        i_file.write(f'{num + 1}. ' + list[num].upper() + '\n')

    i_file.close()

def get_true():
    # открываем файл с решебником
    a_file = open('answers.txt', 'r')

    # создаем список, в который будут считываться решения
    list_1 = []

    answer = a_file.readline()
    answer = answer.rstrip('\n')
    list_1.append(answer)

    # начинаем считывать ответы, отсекая лишнее
    for i in range(19):
        answer = a_file.readline()
        answer = answer.rstrip('\n')
        list_1.append(answer)

    a_file.close()

    return list_1

def get_answers():
    o_file = open('Your answers.txt', 'r') # r для чтения

    list_2 = []

    answer = o_file.readline()
    answer = answer.rstrip('\n')
    list_2.append(answer)

    # начинаем считывать ответы, отсекая лишнее
    for j in range(19):
        answer = o_file.readline()
        answer = answer.rstrip('\n')
        list_2.append(answer)

    o_file.close()

    return list_2

def count_results(list_1, list_2):
    correct = []
    incorrect = []
    right = 0

    for num in range(20):
        if list_1[num] == list_2[num]:
            right += 1
            correct.append(int(num + 1))
        else:
            incorrect.append(int(num + 1))

    print(f'Right answers: {list_1}')
    print(f'Your answers: {list_2}')
    print(f'Counter of right answers: {right}')
    print(f'Numbers of correct questions {correct}')
    print(f'Numbers of incorrect questions {incorrect}')
    if len(correct) >= 15:
        print('Congratulations! You passed the exam')
    else:
        print('You didnt pass the exam')

if __name__ == '__main__':
    main()