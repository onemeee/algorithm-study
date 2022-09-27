import sys
input = sys.stdin.readline

infos = [list(input().split()) for _ in range(int(input()))]
infos.sort(key= lambda x : int(x[0]))
for info in infos:
    print(info[0], info[1])