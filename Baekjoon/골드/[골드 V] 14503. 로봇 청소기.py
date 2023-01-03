import sys
input = sys.stdin.readline

def dfs(i, j, d):
    while True:
        global cnt, n, m
        for k in range(1, 5):
            nd = (d + k) % 4
            ni, nj = i + direction[nd][0], j + direction[nd][1]
            if 0 <= ni< n and 0 <= nj < m:
                if not rooms[ni][nj]:
                    cnt += 1
                    i, j = ni, nj
                    d = nd
                    rooms[i][j] = 2
                    break
        else:
            di, dj = i + direction[(d+2)%4][0], j + direction[(d+2)%4][1]
            if rooms[di][dj] == 2:
                i, j = di, dj
            else:
                break

n, m = map(int, input().split())
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)] # 서 남 동 북
r, c, d = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(n)]
rooms[r][c] = 2
cnt = 1

if d == 0:
    d = 3
elif d == 1:
    d = 2
elif d == 2:
    d = 1
elif d == 3:
    d = 0

dfs(r, c, d)
print(cnt)