#1

week = []
total = 0
for i in range(7):
    week.append(int(input(f'Enter the salary of {i+1} day: ')))
    total+=week[i]
print(week)
print(f'all sales for week is {total}')
