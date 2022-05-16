alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

phrase = str(input('Введите фразу: '))
phrase = phrase.lower()
shift = int(input('Введите количество символов для сдвига: '))
a = str()
b = str()
for i in range(len(phrase)):
        a=a+str(alphabet.index(phrase[i]))+' '
alphabet = alphabet[shift:] + alphabet[:shift]

while len(a) > 0:
    b = b + alphabet[int(a[:a.find(' ')])]
    a = a[a.find(' ')+1:]
print(b)
