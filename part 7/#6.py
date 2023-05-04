a = []

for num in range(5):
    a.append(int(input(f'Enter any number {num+1}: ')))
n = int(input('Lets compare with: '))

b = [i for i in a if i > n]

print(a)
print(b)
print(f'this numbers bigger than {n}: {list(b)}')