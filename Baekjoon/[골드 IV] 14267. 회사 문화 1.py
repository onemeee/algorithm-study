import sys

def praise():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    workers = [0] * n
    superior = list(map(int, input().split()))
    for _ in range(m):
        i, j = map(int, input().split())
        workers[i-1] += j

    for l in range(1, n):
        workers[l] += workers[superior[l]-1]
    print(*workers)

praise()