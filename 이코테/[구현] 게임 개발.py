import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 행, 열, 방향
a, b, d = map(int, input().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

count = 1 # 현재 위치 포함
turn_count = 0

while True:
    if turn_count == 4:
        # 뒤로 갈 방향
        d += 2
        d %= 4
        a -= moves[d][0]
        b -= moves[d][1]
        turn_count = 1
        if maps[a][b] == 1:
            break

    # 왼쪽으로 회전
    turn_left()
    turn_count += 1

    # 회전하고 직전한 경우
    na, nb = a + moves[d][0], b + moves[d][1]
    if 0 <= na < n and 0 <= nb < m:
        # 방문하지 않은 경우
        if not maps[na][nb]:
            count += 1
            maps[na][nb] = 2
            a, b = na, nb
            turn_count = 0
print(count)