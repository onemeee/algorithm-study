def check(list):
    result = 0
    for num in range(1, 10):
        if list.count(num) == 1:
            result = 1
        else:
            result = 0
            break
    return result

for tc in range(1, int(input())+1):
    grid = [list(map(int, input().split())) for _ in range(9)]
    for row in grid:
        result = check(row)
        if result == 0:
            break
    if result == 1:
        grid_rev = [[grid[j][i] for j in range(9)] for i in range(9)]
        for col in grid_rev:
            result = check(col)
            if result == 0:
                break
        if result == 1:
            grid_sm = [grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3] for i in range(0, 7, 3) for j in range(0, 7, 3)]
            for sm in grid_sm:
                result = check(sm)
                if result == 0:
                    break
    print(f'#{tc} {result}')