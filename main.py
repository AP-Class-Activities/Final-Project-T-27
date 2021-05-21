temp = 2
n=int(input())
while n > 1:
    while n % temp == 0:
        n /= temp
    temp = temp + 1
print(temp)
