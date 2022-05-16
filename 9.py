word = str(input('Введите слово: '))
a = word[::-1]
if word == a:
  print("Палиндром")
else:
  print("Нет к сожалению")