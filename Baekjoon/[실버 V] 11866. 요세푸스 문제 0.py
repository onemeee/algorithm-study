n, k = map(int, input().split())
infos = [i for i in range(1, n+1)]
total = n
idx = 0
result = []
while total:
    idx += k-1
    idx %= total
    result.append(infos.pop(idx))
    total -= 1 
print('<' + ', '.join(map(str, result)) + '>')