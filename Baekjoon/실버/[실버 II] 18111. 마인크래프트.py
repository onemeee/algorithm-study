import sys
input = sys.stdin.readline

def find(grid):
    global n, m, b
    max_val = 0
    min_val = 256
    for i in range(n):
        for j in range(m):
            if grid[i][j] < min_val:
                min_val = grid[i][j]
            if grid[i][j] > max_val:
                max_val = grid[i][j]

    min_time = float('INF')
    finalheight = 0
    for height in range(min_val, max_val+1):
        fillbox = 0
        breakbox = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] - height > 0:
                    breakbox += grid[i][j] - height
                else:
                    fillbox +=  height - grid[i][j]
        if fillbox > breakbox + b:
            continue
        else:
            spendtime = breakbox * 2 + fillbox
            if spendtime < min_time:
                finalheight = height
                min_time = spendtime
            elif spendtime == min_time:
                finalheight = height
    print(min_time, finalheight)

n, m, b = map(int, input().split())
grid = [list(map(int, input().rstrip().split())) for _ in range(n)]
find(grid)