import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def rain(info_list):
    if len(info_list) == 1:
        return

    global result
    left = info_list[0]
    right = max(info_list[1:])
    max_idx = info_list[1:].index(right) + 1
    min_val = min(left, right)
    max_val = max(left, right)

    if left == right:
        check = min(info_list)
        if check == left:
            return
    else:
        if left == 0:
            return rain(info_list[max_idx:])
        elif right == 0:
            return

    for i in range(1, max_idx):
        if min_val < info_list[i]:
            min_val = info_list[i]
        elif min_val > info_list[i]:
            result += min_val - info_list[i]

    if max_idx >= len(info_list) - 1:
        return
    else:
        return rain(info_list[max_idx:])

n, m = map(int, input().split())
infos = list(map(int, input().split()))
result = 0
rain(infos)
print(result)