import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
infos = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
result = [0] * (n+1)