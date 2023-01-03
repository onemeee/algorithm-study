import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global n, m, ans
    while q:
        i, j, dis = q.popleft()
        ndis = dis + 1
        for dire in dires:
            ni, nj = i+dire[0], j+dire[1]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                visited[ni][nj] = ndis
                q.append((ni, nj, ndis))
                ans = max(ans, ndis-1)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dires = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
visited = [[0] * m for _ in range(n)]
q = deque()
ans = 0

for i in range(n):
    for j in range(m):
        if grid[i][j]:
            q.append((i, j, 1))
            visited[i][j] = 1
bfs()
print(ans)