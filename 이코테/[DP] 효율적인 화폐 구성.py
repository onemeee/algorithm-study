import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
coins = [ int(input()) for _ in range(n) ]
result = [10001] * (m+1)
for i in range(1, m+1):
    for j in range(n):
        if not i % coins[j]:
            result[i] = min(result[i], i // coins[j])

if result[-1] == 10001:
    print(-1)
else:
    print(result[-1])