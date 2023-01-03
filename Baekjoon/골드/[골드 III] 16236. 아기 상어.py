import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    global n, size, ans
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((i, j, 0))
    grid[i][j] = 0
    visited[i][j] = True
    tmp = 0
    while q:
        i, j, t = q.popleft()
        if tmp:
            if t >= tmp:
                break
        for dire in dires:
            ni, nj = i+dire[0], j+dire[1]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if not grid[ni][nj] or grid[ni][nj]==size:
                    visited[ni][nj]=True
                    q.append((ni, nj, t+1))
                elif grid[ni][nj] < size:
                    visited[ni][nj]=True
                    check.append((ni, nj))
                    tmp = t+1
    ans += tmp

n = int(input())
grid = [list(map(int, input().strip().split())) for _ in range(n)]
dires = [(-1, 0), (0, -1), (0, 1), (1, 0)]
for i in range(n):
    for j in range(n):
        if grid[i][j]==9:
            check = [(i, j)]

ans = 0
size = 2
eat = -1
while check:
    check.sort()
    si, sj = check[0][0], check[0][1]
    eat += 1
    grid[si][sj] = 0
    check = []
    if eat == size:
        size += 1
        eat = 0
    bfs(si, sj)
print(ans)