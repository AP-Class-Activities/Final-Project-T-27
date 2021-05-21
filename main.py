t = 2
n=int(input())
while n > 1:
    while n % t == 0:
        n /= t
    t = t + 1
print(t)
