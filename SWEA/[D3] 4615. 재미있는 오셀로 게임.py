for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    grid = [[0] * n for _ in range(n)]
    grid[n//2-1][n//2] = 1
    grid[n//2][n//2-1] = 1
    grid[n//2-1][n//2-1] = 2
    grid[n//2][n//2] = 2
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, 1, -1, -1, 1]
    for _ in range(m):
        x, y, color = map(int, input().split())
        grid[y-1][x-1] = color
        for i in range(8):
            nx = x-1 + dx[i]
            ny = y-1 + dy[i]
            while True:
                if 0<=nx<n and 0<=ny<n:
                    if color == 1:
                        if grid[ny][nx] == 1:
                            ox = nx - dx[i]
                            oy = ny - dy[i]
                            while grid[oy][ox] == 2:
                                grid[oy][ox] = 1
                                ox -= dx[i]
                                oy -= dy[i]
                            break
                        elif grid[ny][nx] == 2:
                            nx += dx[i]
                            ny += dy[i]
                        else:
                            break
                    elif color == 2:
                        if grid[ny][nx] == 2:
                            ox = nx - dx[i]
                            oy = ny - dy[i]
                            while grid[oy][ox] == 1:
                                grid[oy][ox] = 2
                                ox -= dx[i]
                                oy -= dy[i]
                            break
                        elif grid[ny][nx] == 1:
                            nx += dx[i]
                            ny += dy[i]
                        else:
                            break
                else:
                    break
    cnt = [0, 0]
    for row in grid:
        cnt[0] += row.count(1)
        cnt[1] += row.count(2)
    print(f'#{tc} {cnt[0]} {cnt[1]}')