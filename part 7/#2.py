import random

# win подсмотрел в видеотуториале

win = [0] * 7

for i in range(7):
    win[i] = random.randint(0,9)

print(win)

for i in range(7):
    print(win[i], end=' ')
    print()


# до won догадался сам
won = []

for index in range(7):
    won.append(random.randint(0,9))

print(won)
for index in range(7):
    print(won[index])



