import sys
from collections import deque
input = sys.stdin.readline

def fire(r, c, mg, s, d):
    global n
    dires = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    q = deque()
    q.append((r, c, mg, s, d))
    while q:
        r, c, mg, s, d = q.popleft()
        nr, nc = r+dires[d][0]*s, c+dires[d][1]*s
        grid[nr][nc] += mg
        visited[nr][nc] += 1
        if visited[nr][nc] >= 2:
            if visited[nr][nc] % 2:
                pass

n, m, k = map(int, input().split())
grid = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
for _ in range(m):
    # 행, 열, 질량, 속력, 방향
    r, c, mg, s, d = map(int, input().split())
    
