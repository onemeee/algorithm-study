import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(graph, start, visited):
    global result1
    visited[start] = 1
    for i in graph[start]:
        if not visited[i]:
            result1.append(i)
            dfs(graph, i, visited)

def bfs(graph, start, n):
    global result2
    q = []
    visited2 = [0] * (n+1)
    visited2[start] = 1
    result2.append(start)
    q.append(start)
    while q:
        v = q.pop(0)
        for i in graph[v]:
            if not visited2[i]:
                visited2[i] = 1
                q.append(i)
                result2.append(i)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result1 = [start] # dfs 방문
result2 = [] # bfs 방문
for _ in range(m):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)
for gra in graph:
    gra.sort()
dfs(graph, start, visited)
bfs(graph, start, n)

print(*result1)
print(*result2)