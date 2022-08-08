for TC in range(1, int(input())+1):
    grid = [[0 for j in range(10)] for i in range(10)]
    for i in range(int(input())):
        x1, y1, x2, y2, color = map(int, input().split())
        if color == 1:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if grid[x][y] == 2:
                        grid[x][y] = 3
                    elif grid[x][y] == 0:
                        grid[x][y] = 1
        elif color == 2:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if grid[x][y] == 1:
                        grid[x][y] = 3
                    elif grid[x][y] == 0:
                        grid[x][y] = 2
    violet = 0
    for arr in grid:
        violet += arr.count(3)
    print(f'#{TC} {violet}')