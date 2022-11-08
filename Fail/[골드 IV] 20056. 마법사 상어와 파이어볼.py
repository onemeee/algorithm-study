import sys
input = sys.stdin.readline

def fire(locs, k):
    global n
    dires = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    visited = [[0]*n for _ in range(n)]
    check = [[0]*n for _ in range(n)]
    fast = [[0]*n for _ in range(n)]
    # 행, 열, 질량, 속력, 방향
    for _ in range(k):
        for r, c, m, s, d in locs:
            nr, nc = r+dires[d][0]*s, c+dires[d][1]*s
            grid[nr][nc] += m
            visited[nr][nc] += 1
            fast[nr][nc] += s
            if not check[nr][nc]:
                if d%2:
                    check[nr][nc] = 1
                else:
                    check[nr][nc] = 2
            else:
                if check[nr][nc]%2 and d%2:
                    pass
                elif not check[nr][nc]%2 and not d%2:
                    pass
                else:
                    check[nr][nc] = 0
        locs = []
        for i in range(n):
            for j in range(n):
                if visited[i][j] >= 2:
                    if check[i][j]:
                        for nd in range(0, 7, 2):
                            locs.append((i, j, grid[i][j]//5, fast[i][j]//visited[i][j], nd))
                    else:
                        for nd in range(1, 8, 2):
                            locs.append((i, j, grid[i][j]//5, fast[i][j]//visited[i][j], nd))
                    check[i][j] = 0
                    visited[i][j] = 0
                    fast[i][j] = 0

n, m, k = map(int, input().split())
grid = [[0]*n for _ in range(n)]
locs = []
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    locs.append((r-1, c-1, m, s, d)) 
fire(locs, k)
print(grid)
    
