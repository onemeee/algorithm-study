import sys
input = sys.stdin.readline
n = int(input())
infos = [list(map(int, input().split())) for k in range(n)]

ranks = [0] * n
for i in range(n):
    rank = 1
    lose = 0
    my_w, my_tall = infos[i]
    for j in range(n):
        if i == j:
            continue
        my_tmp = 0
        your_tmp = 0
        your_w, your_tall = infos[j]
        if my_w >= your_w:
            my_tmp += 1
        elif my_w < your_w:
            your_tmp += 1
        if my_tall >= your_tall:
            my_tmp += 1
        elif my_tall < your_tall:
            your_tmp += 1
        if my_tmp < your_tmp:
            lose += 1
    ranks[i] = rank + lose
print(*ranks)

