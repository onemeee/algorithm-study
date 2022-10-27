import sys
input = sys.stdin.readline

def check(info):
    for i in range(n):
        for j in range(n):
            pass

n = int(input())
grid = [[0] * n for _ in range(n)]
infos = [list(map(int, input().split())) for _ in range(n**2)]
locs = [0] * n**2
dires = [(-1, 0), (1, 0), (0, -1), (0, 1)]
