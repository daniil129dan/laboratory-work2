import math
x1 = float(input('Введите первую координату X: '))
y1 = float(input('Введите первую координату Y: '))
x2 = x1
y2 = y1
xi = ' '
yi = 0
a = float()
while xi != '':
    xi = str(input('Введите следующую координату X (Enter для окончания ввода): '))
    if xi != '':
        yi = float(input('Введите следующую координату Y: '))
        a = math.sqrt((float(xi)-x1)**2+(yi-y1)**2)+a
        x1 = float(xi)
        y1 = yi
    else:
        a = math.sqrt((float(x1)-x2)**2+(y1-y2)**2)+a
        break
print(a)
