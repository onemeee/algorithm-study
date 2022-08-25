def bfs(graph, v, visited):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        for i in graph[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
for tc in range(1, int(input())+1):
    node, edge = map(int, input().split())
    graph = [[] for _ in range(node + 1)]
    visited = [0] * (node + 1)
    for _ in range(edge):
        v, w = map(int, input().split())
        graph[v].append(w)
        graph[w].append(v)
    s, g = map(int, input().split())
    bfs(graph, s, visited)
    if visited[g]:
        print(f'#{tc} {visited[g]-1}')
    else:
        print(f'#{tc} 0')