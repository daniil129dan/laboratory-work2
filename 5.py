
a = ' '
while a != '':
    a = str(input())
    if (len(a) == 8):
        if a.count('1') % 2 == 0:
            print('0')
        elif a.count('0') % 2 != 0:
            print('1')

    elif (len(a) != 8)and(a != ''):
        print('ERROR')
    else:
        break

