import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 행, 열, 방향
a, b, d = map(int, input().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0
while True:
    # 왼쪽 방향 바라보기
    d -= 1
    if d == -1:
        d = 3
    a += moves[d][0]
    b += moves[d][1]
    if 0 <= a < n and 0 <= b < m:
        if maps[a][b] == 0:
            result += 1
            maps[a][b] = 2
        else:
            pass
