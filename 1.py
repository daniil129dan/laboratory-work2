x = int(input("Введите целое число (0 для выхода): \n"))
b = 0
i = 0
if x !=0:
    while x != 0:
        b = x+b
        i+=1
        x = int(input())
    print(b//i)
else:
    if i == 0:
        print('error')
