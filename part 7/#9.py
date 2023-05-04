#9 in part 7

import os

def main():

    start = int(input('start: '))
    finish = int(input('finish: '))
    years = get_years()
    x,y = get_choice(start,finish,years)
    # print('---------------------------------')
    # print('years')
    # print(years)
    print(len(years))
    # print('---------------------------------')
    population = get_population()
    # print('---------------------------------')
    print('population', population, len(population))
    # print('---------------------------------')
    difference = get_difference(population)
    get_prints(population,years,x,y,difference)
    # print('---------------------------------')
    print('difference', difference, len(difference))
    # print('---------------------------------')

def get_years():
    years = []
    for i in range(1950,1991):
        years.append(i)
    return years

# создаем переменные, которые ссылаются на индексы в списках, [1950 = 0, 1990 = 40]
def get_choice(start,finish, years):

    x = years.index(start)
    y = years.index(finish)
    return x, y


def get_population():
    # достаем готовые данные для анализа, где первый год 1950
    population = []
    file = open('USPopulation.txt', 'r')
    for line in file:
        number = int(line)
        population.append(number)

    file.close()
    return population
    #выводим результат

    # считаем разницу между годами
def get_difference(population):
    difference = []
    t = 0
    for i in range(0, 40):
        d = population[1 + t] - population[0 + t]
        difference.append(d)
        t += 1
    difference.insert(0,0)

    return difference

def get_prints(population,years,x,y,difference):
    # разница между началом и концом времени по количеству человек
    h = population[y] - population[x]
    print(f'Разница {h} человек')
    result = h / (y - x)
    print(f'Среднегодовое изменение численности {result:.1f} человек в год')
    print(f'Year \t Population \t Difference')
    print('---------------------------------')
    for i in range(x, y+1):
        print(f'{years[x + i]}\t {population[x + i]} \t\t + {difference[x + i]}')
    print('---------------------------------')
    print(f'minimum was in {min(difference[x:y])}')
    print(f'maximum was in {max(difference[x:y])}')
if __name__ == '__main__':
    main()


