import sys
input = sys.stdin.readline

def check(i, j):
    global n, m, mount
    # 8가지 방향 확인
    dires = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    max_val = maps[i][j]
    visited[i][j] = 1

    for dx, dy in dires:
        ni, nj = i + dx, j + dy
        if 0 <= ni < n and 0 <= nj < m:
            # 인접한 격자보다 작으면
            if max_val < maps[ni][nj]:
                mount = False
            if max_val == maps[ni][nj] and not visited[ni][nj]:
                check(ni, nj)

count = 0
n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
mount = False
for i in range(n):
    for j in range(m):
        if maps[i][j] and not visited[i][j]:
            mount = True
            check(i, j)  
            if mount:
                count += 1

print(count)