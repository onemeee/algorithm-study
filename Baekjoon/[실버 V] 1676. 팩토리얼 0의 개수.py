n = int(input())

i = 1
num = 0
while n >= 5**i:
    num += n//5**i
    i += 1
print(num)