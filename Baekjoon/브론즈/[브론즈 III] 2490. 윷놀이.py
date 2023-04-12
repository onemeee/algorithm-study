import sys
input = sys.stdin.readline


def result(arr):
    cnt = 0
    for val in arr:
        if val == 0:
            cnt += 1
    if cnt == 0:
        return 'E'
    if cnt == 1:
        return 'A'
    if cnt == 2:
        return 'B'
    if cnt == 3:
        return 'C'
    if cnt == 4:
        return 'D'


for _ in range(3):
    info = list(map(int, input().rstrip().split()))
    print(result(info))
