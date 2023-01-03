import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
drawing = [ list(map(int, input().split())) for _ in range(n)]
area = [ [0] * m for _ in range(n)]
max_val = 0
dires = [(0, 1), (1, 0), (0, -1), (-1, 0)]
num = 0

# 최고 넓이
max_area = 0

def dfs(i, j):
    global tmp_area
    drawing[i][j] = 0
    tmp_area += 1
    for dire in dires:
        ni = dire[0] + i
        nj = dire[1] + j
        if 0 <= ni < n and 0 <= nj < m:
            if drawing[ni][nj]:
                dfs(ni, nj)

for i in range(n):
    for j in range(m):
        if drawing[i][j]:
            tmp_area = 0
            num += 1
            dfs(i, j)
            max_area = max(max_area, tmp_area)

print(num)
print(max_area)
