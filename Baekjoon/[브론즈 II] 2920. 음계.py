info = list(map(int, input().split()))
if info[0] == 1:
    result = 'ascending'
    for i in range(1, 8):
        if info[i] != i+1:
            result = 'mixed'
elif info[0] == 8:
    result = 'descending'
    for i in range(1, 8):
        if info[i] != 8-i:
            result = 'mixed'
else:
    result = 'mixed'
print(result)