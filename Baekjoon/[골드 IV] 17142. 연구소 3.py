import sys
from collections import deque 
from pprint import pprint
input = sys.stdin.readline

def findvirus():
    global n, cnt
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                virus.append((i, j))
                cnt += 1
            elif grid[i][j] == 1:
                cnt += 1

def bfs(vir):
    global n, tmp
    visited = [[0] * n for _ in range(n)]
    q = deque()
    dires = [(-1,0), (1,0), (0,1), (0,-1)]
    for i, j in vir:
        q.append((1, i, j))
        visited[i][j] = 'v'
    if tmp == n*n:
        return 0
    while q:
        t, i, j = q.popleft()
        for dire in dires:
            nt, ni, nj = t+1, i+dire[0], j+dire[1]
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] != 1 and not visited[ni][nj]:
                if not grid[ni][nj]:
                    visited[ni][nj] = nt
                    q.append((nt, ni, nj))
                    tmp += 1
                    if tmp == n*n:
                        return nt-1
                elif grid[ni][nj] == 2:
                    visited[ni][nj] = nt
                    q.append((nt, ni, nj))
    return t-1
            
def combi(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]]
        else:
            for next in combi(arr[i+1:], k-1):
                yield [arr[i]] + next

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
virus = []
cnt = 0 
ans = float('INF')
findvirus()
for vir in combi(virus, m): 
    tmp = cnt
    t = bfs(vir)
    if tmp == n*n:
        ans = min(ans, t)
if ans == float('INF'):
    print(-1)
else:
    print(ans)