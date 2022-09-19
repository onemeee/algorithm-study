from collections import deque
import sys
input = sys.stdin.readline

def findtoma(m,n, arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                locs.append((j,i))
                

def findxy(locs):
    global day
    location = deque()
    if locs:
        day += 1
        for loc in locs:
            x, y = loc[0], loc[1]
            for k in dxdy:
                dx, dy = k[0], k[1]
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0<= ny < n:
                    if not tomato[ny][nx]:
                        location.append((nx,ny))
        return location
    return 0

def bfs(que):
    while que:
        x, y = que.popleft()
        tomato[y][x] = 1
        locs.append((x,y))

def check(tomato):
    global day
    for toma in tomato:
        if 0 in toma:
            day = 0

m, n = map(int, input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]
dxdy = [[1,0], [0,1], [-1,0], [0,-1]]
locs = deque()
findtoma(m, n, tomato)
day = 0
while True:
    que = findxy(locs)
    if que:
        bfs(que)
    else:
        break
check(tomato)
print(day-1)

