import sys
from collections import deque
input = sys.stdin.readline

def find(grid, n):
    loc = []
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                loc.append((grid[i][j], i,j))
    return sorted(loc)

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
locs = find(grid, n)
s, x, y = map(int, input().split())
for _ in range(s):
    for _ in range(len(locs)):
        num, i, j = locs.pop(0)
        for dire in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + dire[0]
            nj = j + dire[1]
            if 0<= ni < n and 0 <= nj < n and not grid[ni][nj]:
                grid[ni][nj] = num
                locs.append((num, ni, nj))
print(grid[x-1][y-1])