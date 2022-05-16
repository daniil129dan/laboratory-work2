a = 3
print(a)
i = 0
b = 2
for i in range(14):
    if i % 2 == 0:
        a = a + 4/(b*(b+1)*(b+2))
        print(a)
    elif i % 2 != 0:
        a = a - 4/(b*(b+1)*(b+2))
        print(a)
    b = b+2