from collections import deque

n, m = map(int, input().split())
maps = [ list(map(int, input().rstrip())) for _ in range(n) ]

visited = [ [0] * m for _ in range(n)]
def bfs():
    global n, m

    visited[0][0] = 1
    que = deque([(0, 0)])
    dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while que:
        # 현재 위치
        ci, cj = que.popleft()
        for di, dj in dires:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m:
                if maps[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = visited[ci][cj] + 1
                    que.append((ni, nj))
    
bfs()
print(visited[n-1][m-1])