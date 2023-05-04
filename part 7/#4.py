line = []
total = 0
for num in range(20):
    line.append(int(input(f'Enter number {num+1}: ')))
    total += line[num]

print(f'the min is {min(line)}; '
      f'the max is {max(line)}; '
      f'sum is {total}; '
      f'average is {total/len(line)}')