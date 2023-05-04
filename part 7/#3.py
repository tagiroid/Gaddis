year = []

total = 0
for month in range(12):
    year.append(int(input(f'Enter the amount of precipitations for {month+1}: ')))
    total += year[month]


print(year)
print(f'total precipitations are {total}')
print(f'min is {min(year)}')
print(f'max is {max(year)}')