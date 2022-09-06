n, m = map(int, input().split())

cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
        if cnt == m:
            print(i)
            break
if cnt < m:
    print(0)