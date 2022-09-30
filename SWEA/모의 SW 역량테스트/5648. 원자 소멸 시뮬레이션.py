from collections import deque
for tc in range(1, int(input())+1):
    n = int(input())
    que = deque(list(map(int, input().split())) for _ in range(n))
    visited = [[0] * 2000 for _ in range(2000)]
    
    while que:
        x, y, d, k = que.popleft()
        print(x, y, d, k)
    print(f'#{tc}')