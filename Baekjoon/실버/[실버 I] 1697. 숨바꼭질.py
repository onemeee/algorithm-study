import sys
from collections import deque
input = sys.stdin.readline


def bfs(n, k):
    visited = [0] * 100001 
    q = deque()
    q.append((n, 0))
    visited[n] = 1
    while q:
        x, t = q.popleft()
        if x == k:
            return t
        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx < 100001 and not visited[nx]:
                visited[nx] = 1
                q.append((nx, t+1))

n, k = map(int, input().split())
print(bfs(n, k))