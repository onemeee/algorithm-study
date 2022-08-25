import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    cnt = 0
    i = 1
    while 5**i <= n:
        cnt += n // 5**i
        i += 1
    print(cnt)