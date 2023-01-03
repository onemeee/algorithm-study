import sys
sys.setrecursionlimit(10**9) # 재귀 깊이 임의로 늘려주기

import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)

N, M = map(int, input().split())
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for start in range(1, N+1):
    visited2 = visited.copy()
    dfs(graph, start, visited)
    if visited2 != visited:
        cnt += 1
print(cnt)