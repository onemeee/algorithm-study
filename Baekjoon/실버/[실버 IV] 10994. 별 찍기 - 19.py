n = int(input())
grid = [[' '] * (4*n-3) for _ in range(4*n-3)]
# n: 반복 횟수, x,y : 시작점
def star(n, x, y):
    if n == 1:
        grid[x][y] ='*'
        return
    for i in range(4*n-3):
        for j in range(4*n-3):
            if (i == 0) or (i==4*n-4):
                grid[x+i][y+j] = '*'
            else:
                grid[x+i][y] = '*'
                grid[x+i][y+4*n-4] = '*'
                break
    star(n-1, x+2, y+2)
star(n, 0, 0)
for ans in grid:
    print(''.join(ans))