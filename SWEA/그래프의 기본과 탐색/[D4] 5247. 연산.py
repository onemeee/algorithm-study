from collections import deque

def bfs(n, m):
    global ans
    visited = [0] * 1000001
    visited[n] = 1
    q = deque()
    q.append((n, 1))

    while q:
        n, cnt = q.popleft()
        for cn in [n+1, n-1, n*2, n-10]:
            if 0 < cn <= 1000000 and not visited[cn]:
                if cn == m:
                    return cnt
                visited[cn] = 1
                q.append((cn, cnt+1))
                
for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    ans = bfs(n, m)
    print(f'#{tc} {ans}')