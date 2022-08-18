def DFS(graph, start, visited):
    visited[start-1] = 1
    for i in graph[start-1]:
        if visited[i-1] == 0:
            DFS(graph, i, visited)

for TC in range(1, int(input())+1):
    V, E = map(int, input().split()) # 노드의 개수, 간선의 개수
    info = [[] for _ in range(V)]
    visited = [0] * V
    result = 0
    # 각 노드의 연결지점 체크
    for _ in range(E): 
        node, edge = map(int, input().split())
        info[node-1].append(edge)
    
    start, end = map(int, input().split())
    
    DFS(info, start, visited)
    if visited[end-1] == 1:
        result = 1

    print(f'#{TC} {result}')