import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find(m, n):
    global result
    dis = distances[m]
    for i in range(1, len(dis)):
        if dis[i] and not visited[m][i]:
            visited[m][i] = 1
            visited[i][m] = 1
            find(i, n+dis[i])
            visited[m][i] = 0
            visited[i][m] = 0
    else:
        result = max(result, n)


result = 0
n = int(input())
distances = [[0] * (n+1) for _ in range(n+1)]
visited = [[0] * (n+1) for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    distances[a][b] = c
    distances[b][a] = c    
find(1, 0)
print(result)
