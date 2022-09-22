def dfs(i, j):
    for dire in direction:
        ni, nj = i + dire[0], j + dire[1]
        if 0 <= ni < n and 0 <= nj < n:
            tmp = sum_val[i][j] + grid[ni][nj]
            if not sum_val[ni][nj]:
                sum_val[ni][nj] = tmp
                dfs(ni, nj)
            elif tmp < sum_val[ni][nj]:
                sum_val[ni][nj] = tmp
                dfs(ni, nj)

for tc in range(1, int(input())+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    sum_val = [[0]*n for _ in range(n)]
    sum_val[0][0] = grid[0][0]
    direction = [[1,0], [0,1]]
    dfs(0, 0)
    print(f'#{tc} {sum_val[n-1][n-1]}')