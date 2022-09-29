def dfs(v):
    global tmp
    if visited[v]:
        return
    visited[v] = 1
    tmp += 1
    for w in graph[v]:
        if not visited[w]:
            tmp += 1
            dfs(w)

    
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    infos = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        graph[infos[2*i]].append(infos[2*i+1])
        graph[infos[2*i+1]].append(infos[2*i])
    visited = [0] * (n+1)
    ans = 0
    for j in range(1, n+1):
        tmp = 0
        dfs(j)
        if tmp:
            ans += 1
    print(f'#{tc} {ans}')