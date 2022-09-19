from collections import deque
import sys
input = sys.stdin.readline

def finday():
    total = 0
    locs = deque()
    day = 0
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                total += 1
                locs.append((j,i,day))
            elif tomato[i][j] == -1:
                total += 1
    while locs:
        x, y, day = locs.popleft()
        for k in dxdy:
            nx, ny = x+k[0], y+k[1]
            if 0 <= nx < m and 0<= ny < n and not tomato[ny][nx]:
                tomato[ny][nx] = 1
                total+=1
                locs.append((nx, ny, day+1))
    return total, day

m, n = map(int, input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]
dxdy = [[1,0], [0,1], [-1,0], [0,-1]]
total, day = finday()

if total == m*n:
    print(day)
else:
    print(-1)

