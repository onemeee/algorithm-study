def DFS(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            DFS(graph, i, visited)

N = int(input())
visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(int(input())):
    val1, val2 = map(int, input().split())
    graph[val1].append(val2)
    graph[val2].append(val1)

DFS(graph, 1, visited)
result = visited.count(1) - 1 # 1번 컴퓨터 제외
print(result)
