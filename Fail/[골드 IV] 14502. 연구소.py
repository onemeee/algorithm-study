import sys
input = sys.stdin.readline

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(cnt, sx, sy):
    if cnt == 3:
        return

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]