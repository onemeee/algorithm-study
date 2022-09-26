n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
min_val = 50 * 50
for row in range(n-7):
    for col in range(m-7):
        tmp_grid = [grid[row+k][col:col+8] for k in range(8)]
        tmp1 = 0
        tmp2 = 0
        for i in range(8):
            for j in range(8):
                if i%2:
                    if j%2:
                        if tmp_grid[i][j] != 'W':
                            tmp1 += 1
                        else:
                            tmp2 += 1
                    else:
                        if tmp_grid[i][j] != 'B':
                            tmp1 += 1
                        else:
                            tmp2 += 1
                else:
                    if j%2:
                        if tmp_grid[i][j] != 'B':
                            tmp1 += 1
                        else:
                            tmp2 += 1
                    else:
                        if tmp_grid[i][j] != 'W':
                            tmp1 += 1
                        else:
                            tmp2 += 1
        tmp = min(tmp1, tmp2)
        min_val = min(min_val, tmp)
print(min_val)