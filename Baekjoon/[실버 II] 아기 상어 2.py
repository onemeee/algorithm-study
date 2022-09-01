import sys
input = sys.stdin.readline
dx = [1, 1, -1, -1, 0, 0, -1, 1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

def bfs(x,y):
    visited = [[0]*m for _ in range(n)]
    q = []
    q.append((x,y))
    while q:
        x, y = q.pop(0)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny>= m:
                continue
            else:
                if not visited[nx][ny]:
                    if grid[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y] + 1
                    else:
                        q.append((nx, ny))
        print(visited)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    for j in range(m):
        bfs(i, j)