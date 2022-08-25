def bfs(sx, sy):
    result = 0
    q = []
    q.append((sx, sy))
    while q:
        x, y = q.pop()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if maze[nx][ny] == '1':
                        continue
                    elif maze[nx][ny] == '0':
                        q.append((nx, ny))
                    elif maze[nx][ny] == '3':
                        result = 1
                        break
    return result

for tc in range(1, 11):
    t = input()
    maze = [list(input()) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                sx, sy = i, j
    result = bfs(sx, sy)
    print(f'#{tc} {result}')