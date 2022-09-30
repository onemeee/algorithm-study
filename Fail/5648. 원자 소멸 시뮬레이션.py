from collections import deque
for tc in range(1, int(input())+1):
    n = int(input())
    que = deque()
    for _ in range(n):
        x, y, d, t = map(int, input().split())
        x += 1000
        y += 1000
        que.append((x, y, d, t, 0))
    visited = [[0] * 2001 for _ in range(2001)]
    
    while que:
        x, y, d, k, t = que.popleft()
        if d == 0:
            pass
        elif d == 1:
            pass
        elif d == 2:
            pass
        elif d == 3:
            pass
    print(f'#{tc}')