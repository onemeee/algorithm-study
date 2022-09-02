from collections import deque
import sys

input = sys.stdin.readline
dx = [1, 1, -1, -1, 0, 0, -1, 1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def bfs(x,y):
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    if grid[x][y] == 1:
        return 0
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny>= m:
                continue
            else:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    if grid[nx][ny] == 1:
                        return visited[nx][ny]-1
                    else:
                        q.append((nx, ny))

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_dis = 0
for i in range(n):
    for j in range(m):
        dis = bfs(i, j)
        if dis:
            max_dis = max(max_dis, dis)  
print(max_dis)
