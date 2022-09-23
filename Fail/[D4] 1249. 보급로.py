def find(i, j, total):
    global result
    if total > result:
        return
    if i == n-1 and j == n-1:
        result = min(result, total)
        return
    for dire in direction:
        ni, nj = i+dire[0], j+dire[1]
        if 0 <= ni < n and 0 <= nj < n:
            tmp = total + grid[ni][nj]
            if not visited[ni][nj]:
                visited[ni][nj] = 1
                find(ni, nj, tmp)
                visited[ni][nj] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    grid = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    visited[0][0] = 1
    direction = [[1, 0], [0, 1], [-1, 0], [0,- 1]]
    result = 100 * 100 * 10
    find(0, 0, 0)
    print(f'#{tc} {result}')