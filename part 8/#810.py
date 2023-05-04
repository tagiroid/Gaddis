# решение взято из нашего любимого интернета
# string = 'fgfhsadsssssllfd'
# counted_chars = {}

# for char in string:
#     if char in counted_chars:
#        counted_chars[char] += 1
 #    else:
#        counted_chars[char] = 1

# print(max(counted_chars),counted_chars)

string = 'fgfhsadsssssllfds'
mylist = []

for letter in string:
    mylist.append(letter)
print(mylist)
while len(mylist) > 1:
    for letter in mylist:
        if letter in mylist:
            del letter


print(mylist)
