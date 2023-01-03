import sys
input = sys.stdin.readline
grid = [[0] * 1001 for _ in range(1001)]
n = int(input())
count = [0] * n
for i in range(1, n+1):
    x, y, w, h = map(int, input().split())
    count[i-1] = w*h
    for nx in range(x, x+w):
        for ny in range(y, y+h):
            if grid[nx][ny]:
                count[grid[nx][ny]-1] -= 1
            grid[nx][ny] = i
for ans in count:
    print(ans)
