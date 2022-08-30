import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    garden[x][y] = 0
    q = []
    q.append((x, y))
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            elif garden[nx][ny] == 1:
                garden[nx][ny] = 0
                q.append((nx, ny))
for _ in range(int(input())):
    cnt = 0
    M, N, K = map(int, input().split())
    garden = [[0] * M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        garden[i][j] = 1
    for i in range(N):
        for j in range(M):
            if garden[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)