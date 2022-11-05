import sys
from pprint import pprint
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

locs = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
dires = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def rain(d, s):
    global n, m
    visited = [[0] * n for _ in range(n)]
    tmps = []
    for loc in locs:
        i, j = (loc[0] + dires[d][0]*s) % n, (loc[1] + dires[d][1]*s) % n
        grid[i][j] += 1
        visited[i][j] = True
        tmps.append((i,j))
    
    for tmp in tmps:
        cnt = 0
        ci, cj = tmp[0], tmp[1] 
        for k in range(1, 8, 2):
            ni, nj = ci+dires[k][0], cj+dires[k][1]
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj]:
                cnt += 1
        grid[ci][cj] += cnt
    locs.clear()
    # 구름 생길 곳 찾아주기
    for p in range(n):
        for q in range(n):
            if not visited[p][q] and grid[p][q] >= 2:
                grid[p][q] -= 2
                locs.append((p, q))


for l in range(m):
    d, s = map(int, input().split())
    rain(d-1, s)

ans = 0
for i in range(n):
    for j in range(n):
        ans += grid[i][j]
print(ans)
