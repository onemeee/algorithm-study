grid = [[0] * 100 for _ in range(100)]
cnt = 0
for _ in range(int(input())):
    col, row = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if grid[row+i][col+j] == 0:
                grid[row+i][col+j] = 1
                cnt += 1
print(cnt)