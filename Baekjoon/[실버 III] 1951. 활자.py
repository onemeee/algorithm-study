import sys
input = sys.stdin.readline

n = int(input())
m = len(str(n))
result = 0
tmp = 1
tmp2 = 0
for i in range(m):
    if m == 1:
        result += 1 * n
        break
    if i == m-1:
        result += tmp * (n-tmp2)
        break
    tmp2 += 9*(10**i)
    result += tmp * 9*(10**i)
    tmp += 1

print(result%1234567)


