def sumcol(list, i, j, K):
    sum = 0
    for k in range(i, K):
        sum += list[k][j]
    return sum
    
def findmax(list):
    max_val = 0
    for vals in list:
        for val in vals:
            if val > max_val:
                max_val = val
    return max_val

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    sum_list = [[0] * (N-M+1) for _ in range(N-M+1)]
    init_grid = []
    for i in range(M):
        init_grid += grid[i][0:M]
    sum_list[0][0] = sum(init_grid) # 초기값 입력
    for j in range(N-M+1):
        for i in range(N-M+1):
            if i or j:
                if i == 0:
                    sum_list[i][j] = sum_list[i][j-1] + sumcol(grid, i, j+M-1, M) - sumcol(grid, i, j-1, M)
                else:
                    sum_list[i][j] = sum_list[i-1][j] + sum(grid[i+M-1][j:j+M]) - sum(grid[i-1][j:j+M])
    result = findmax(sum_list)
    print(f'#{tc} {result}')