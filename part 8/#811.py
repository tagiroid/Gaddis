# ОстановисьИПочувствуйЗапахРоз

mystr = 'ОстановисьИПочувствуйЗапахРоз'
res = []
for letter in mystr:
    if letter.islower():
        res.append(letter)
    if letter.isupper():
        res.append(' ')
        res.append(letter)

print(''.join(res).lower().lstrip().capitalize())
