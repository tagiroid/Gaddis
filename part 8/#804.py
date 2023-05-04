# Not all of the elements are important.
# What you need to do here is to remove
# from the list all of the elements before the given one.
mystr = input('Text: ').lower()
morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
         'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.-', 'z': '--..', '1': '.----',
         '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
         '9': '----.', '0': '-----', '?': '..--..', '.': '.-.-.-', ',': '--..--', ' ': ' '}

res = []
for letter in mystr:
    res.append(morse.get(letter))

print(' '.join(res))