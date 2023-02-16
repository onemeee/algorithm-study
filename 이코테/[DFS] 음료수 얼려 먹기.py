import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ices = [ list(map(int, list(input().rstrip()))) for _ in range(n)]

def dfs(i, j):
    global n, m
    dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for di, dj in dires:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and not ices[ni][nj]:
            ices[ni][nj] = 1
            dfs(ni, nj)

count = 0

for i in range(n):
    for j in range(m):
        if not ices[i][j]:
            ices[i][j] = 1
            dfs(i, j)
            count += 1

print(count)