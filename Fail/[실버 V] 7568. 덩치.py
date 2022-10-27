import sys
input = sys.stdin.readline
n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]
infos.sort(reverse=True)
print(infos)