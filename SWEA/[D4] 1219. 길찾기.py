def DFS(graph, start, vistied):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            DFS(graph, i, vistied)
        
for tc in range(1, 11):
    TC, leng = map(int, input().split())
    info = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visited = [0] * 100
    result = 0

    # 경로 표시
    for i in range(leng):
        graph[info[2*i]].append(info[2*i+1])
    DFS(graph, 0, visited)
    if visited[99] == 1:
        result = 1
    print(f'#{TC} {result}')