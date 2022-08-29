n = int(input())
result = 0
if n % 5 == 0:
    result += n //5
else:
    bag = 0
    while n >= 0:
        n -= 3
        bag += 1
        if n % 5 == 0:
            result += n//5
            result += bag
            break
    if n < 0:
        result = -1
print(result)
