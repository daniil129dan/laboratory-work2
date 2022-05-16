n = float(input())
x = n
guess = (x+1)/2
while guess<x:
    x = guess
    guess = (x + n / x) / 2
print(x)
