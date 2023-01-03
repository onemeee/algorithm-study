import sys
input = sys.stdin.readline

for _ in range(int(input())):
    point = -1
    n, idx = map(int, input().rstrip().split())
    que = list(map(int, input().rstrip().split()))
    max_val = max(que)
    ans = 0
    while True:
        point += 1
        point %= n
        if que[point] == max_val:
            if point == idx:
                ans += 1
                break
            que[point] = 0
            ans += 1
            max_val = max(que)
    print(ans)
