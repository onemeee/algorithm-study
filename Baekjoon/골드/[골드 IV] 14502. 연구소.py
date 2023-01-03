import sys
from collections import deque
input = sys.stdin.readline

def combi(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]]
        else:
            for next in combi(arr[i+1:], k-1):
                yield [arr[i]] + next

def bfs(i, j):
    global n, m, cnt
    dires = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    q.append((i, j))
    visited[i][j] = 2
    cnt += 1
    while q:
        i, j = q.popleft()
        for dire in dires:
            ni, nj = i + dire[0], j + dire[1]
            if 0 <= ni < n and 0 <= nj < m and not grid[ni][nj] and not visited[ni][nj]:
                    cnt += 1
                    visited[ni][nj] = 2
                    q.append((ni, nj))


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
virus = []
walls = []
wall_val = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            virus.append((i, j))
        elif not grid[i][j]:
            walls.append((i,j))
        else:
            wall_val += 1
ans = 0
for wall in combi(walls, 3):
    cnt = wall_val + 3
    visited = [[0] * m for _ in range(n)]
    for wal in wall:
        grid[wal[0]][wal[1]] = 1
    for vir in virus:
        bfs(vir[0], vir[1])
    for wal in wall:
        grid[wal[0]][wal[1]] = 0
    ans = max(ans, n*m-cnt)
print(ans) 
