import sys
input = sys.stdin.readline

infos = [list(map(int, input().split())) for _ in range(int(input()))]
infos.sort(key= lambda x : (x[0], x[1]))
for info in infos:
    print(*info)