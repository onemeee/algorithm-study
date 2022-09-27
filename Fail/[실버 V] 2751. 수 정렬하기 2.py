import sys
input = sys.stdin.readline

n = int(input())
infos = [int(input())for _ in range(n)]
for i in range(n):
    min_val = infos[i]
    min_idx = i
    for j in range(i+1, n):
        if infos[j] < min_val:
            min_idx = j
            min_val = infos[j]
    infos[i], infos[min_idx] = infos[min_idx], infos[i]
for info in infos:
    print(info)