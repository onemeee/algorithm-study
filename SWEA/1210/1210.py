# 시작 찾기 함수 정의
def findstart(grid, row, col):
            # 상, 우, 좌
    delta = [[-1,0], [0, 1], [0, -1]]
    direction = 0
    while row != 0:
        row += delta[direction][0]
        col += delta[direction][1]
        if direction == 0:
            if grid[row][col+1]:
                direction = 1
            elif grid[row][col-1]:
                direction = 2
        else:
            if grid[row-1][col] == 1:
                direction = 0
    return col-1

for TC in range(1, 11):
    N = int(input())
    grid = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    row = 99
    for y in range(102):
        if grid[row][y] == 2:
            col = y
    result = findstart(grid, row, col)

    print(f'#{TC} {result}')