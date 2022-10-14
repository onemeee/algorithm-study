def check(i, j, dire):
    cnt = 0
    global n
    ni, nj = i + dire[0], j + dire[1]
    while 0 <= ni < n and 0 <= nj < n:
        if grid[ni][nj]:
            return False
        ni += dire[0]
        nj += dire[1]
        cnt += 1
    return cnt

def connect(i, j, dire):
    global n
    ni, nj = i + dire[0], j + dire[1]
    while 0 <= ni < n and 0 <= nj < n:
        grid[ni][nj] = 2
        ni += dire[0]
        nj += dire[1]

def delete(i, j, dire):
    global n
    ni, nj = i + dire[0], j + dire[1]
    while 0 <= ni < n and 0 <= nj < n:
        grid[ni][nj] = 0
        ni += dire[0]
        nj += dire[1]

def dfs(idx, core, wire):
    global m, max_core, min_wire
    if core > max_core:
        max_core = core
        min_wire = wire
    elif core == max_core:
        min_wire = min(min_wire, wire)
    if core + m - idx < max_core:
        return
    if idx == m:
        return
    i, j = cores[idx]
    for dire in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        flag = check(i, j, dire)
        if flag:
            connect(i, j, dire)
            nwire = wire + flag
            dfs(idx+1, core+1, nwire)
            delete(i, j, dire)
        else:
            dfs(idx+1, core, wire)


for tc in range(1, int(input())+1):
    n = int(input())
    grid = [ list(map(int, input().split())) for _ in range(n) ]
    cores = []
    for i in range(1, n-1):
        for j in range(1, n-1):
            if grid[i][j] == 1:
                cores.append((i, j))
    max_core = 0
    min_wire = 12*12
    m = len(cores)
    dfs(0, 0, 0)
    print(f'#{tc} {min_wire}')