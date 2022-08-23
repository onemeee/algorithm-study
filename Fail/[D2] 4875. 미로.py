for tc in range(1, int(input())+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    for row in grid:
        for i in row:
            if i == 3:
                start = (row, i)
                break