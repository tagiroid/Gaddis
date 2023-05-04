import os

text = open('text.txt', 'r')

lines = text.readlines()
sentences = []

for line in lines:
    line = line.rstrip('\n')
    sentences.append(line)

words = []
for sentence in sentences:
    sentence = sentence.split()
    words.append(len(sentence))
text.close()

print(words)
print(sum(words)/len(words))

