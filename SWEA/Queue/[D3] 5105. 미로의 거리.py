def bfs(sx, sy, ex, ey):
    queue = []
    queue.append((sx,sy))
    while queue:
        sx, sy = queue.pop(0)
        visit[sx][sy] = 1
        for i in range(4):
            nx, ny = sx + dx[i], sy + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >= n:
                    continue
            if not visit[nx][ny]:
                if grid[nx][ny] == '1':
                    continue
                elif grid[nx][ny] == '0':
                    dis[nx][ny] = dis[sx][sy] + 1
                    queue.append((nx,ny))
                elif  grid[nx][ny] == '2':
                    dis[nx][ny] = dis[sx][sy]

for tc in range(1, int(input())+1):
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    dis = [[0] * n for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '3':
                sx, sy = i, j
            if grid[i][j] == '2':
                ex, ey = i, j
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    bfs(sx, sy, ex, ey)
    print(f'#{tc} {dis[ex][ey]}')