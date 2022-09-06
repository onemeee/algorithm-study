import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    idx_list = []
    idx = 0
    while n != 0:
        if n%2:
            idx_list.append(idx)
        n //= 2
        idx += 1
    print(*idx_list)