def dfs(i, cnt):
    global n
    visited[i] = 1
    dires = [infos[i], -1 * infos[i]]
    for dire in dires:
        ni = i + dire
        if 0 <= ni < n and not visited[ni]:
            dfs(ni, cnt+1)
n = int(input())
infos = list(map(int, input().split()))
visited = [0] * n
s = int(input()) - 1
dfs(s, 0)
ans = sum(visited)
print(ans)