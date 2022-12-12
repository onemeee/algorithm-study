import sys
from collections import deque
input = sys.stdin.readline

def praise():
    n, m = map(int, input().split())
    workers = [0] * n
    superior = list(map(int, input().rstrip().split()))
    for _ in range(m):
        i, j = map(int, input().split())
        workers[i-1] += j

    for i in range(n):
        if superior[i] == -1:
            continue
        workers[i] += workers[superior[i]-1]
    print(*workers)

praise()