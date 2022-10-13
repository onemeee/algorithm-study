import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().split()) for _ in range(n)]
cnt = 0
# 빨간색 공의 x, y, 파란색 공의 x, y, cnt
info = deque()
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            pass