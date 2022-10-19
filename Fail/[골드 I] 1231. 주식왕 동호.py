import sys
input = sys.stdin.readline

def dfs(Ms, val, i):
    global max_val
    max_val = max(max_val, val)
    for idx in check:
        tmp = prices[idx][i]
        if Ms >= tmp:
            dfs(Ms-tmp, val + prices[idx][i+1]-prices[idx][i], i)
                

N, L, Ms = map(int, input().split())
prices = [ list(map(int, input().split())) for _ in range(N) ]
for i in range(L-1):
    max_val = 0
    check = []
    for j in range(N):
        price = prices[j]
        if price[i] < price[i+1]:
            check.append(j)
    if check:
        dfs(Ms, 0, i)
        Ms += max_val
print(Ms)