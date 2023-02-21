import sys
input = sys.stdin.readline

n = int(input())
infos = []
max_p = 0

def dfs(t, p):
    global n, max_p
    if t >= n:
        max_p = max(max_p, p)
        return
    # 일하는 경우
    if t+infos[t][0] <= n:
        dfs(t+infos[t][0], p+infos[t][1])

    # 일하지 않는 경우
    dfs(t+1, p)

for k in range(n):
    t, p = map(int, input().rstrip().split())
    infos.append((t, p))
    
dfs(0, 0)
print(max_p)