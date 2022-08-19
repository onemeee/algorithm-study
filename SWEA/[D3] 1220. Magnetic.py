for TC in range(1, 11):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    grid = [[info[i][j] for i in range(N)] for j in range(N)]
    stack = []
    result = 0
    for i in range(N): # 한 줄씩 체크
        if (1 and 2) in grid[i]: # 1, 2가 함께 있는 경우 탐색
            for j in range(N):
                if grid[i][j] == 1 or grid[i][j] == 2:
                    if stack:
                        if stack[-1] == grid[i][j]:
                            stack.pop()
                    stack.append(grid[i][j])
        if stack[0] != 2:
            result += stack.count(2)
        else:
            result += stack.count(2) - 1
        stack.clear()
    print(f'#{TC} {result}')