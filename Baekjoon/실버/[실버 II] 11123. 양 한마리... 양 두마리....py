import sys
from collections import deque
input = sys.stdin.readline

def check(i, j, grid):
    global h, w

    dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    que = deque([(i, j)])
    grid[i][j] = '.'
    visited[i][j] = 0

    while que:
        ci, cj = que.popleft()
        for dx, dy in dires:
            ni, nj = ci + dx, cj + dy
            if 0 <= ni < h and 0 <= nj < w:
                if grid[ni][nj] == '#' and not visited[ni][nj]:
                    visited[ni][nj] = 0
                    que.append((ni, nj))
                    grid[ni][nj] = '.'

tc = int(input())

for _ in range(tc):
    h, w = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            # 양이 있으면
            if grid[i][j] == '#' and not visited[i][j]:
                # 무리 전부 탐색
                check(i, j, grid)
                count += 1
    print(count)