n = int(input())
result = 0
result += n//5
remain = n%5
if remain == 0:
    pass
else:
    result += remain//3
    remain %= 3
    if remain:
        if n%3==0:
            result = n//3
        else:
            result = -1
print(result)
