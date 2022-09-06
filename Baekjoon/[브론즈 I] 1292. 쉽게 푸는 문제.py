n, m = map(int, input().split())
sum_val = 0
cnt = 0
for i in range(1, m+1):
    for _ in range(i):
        cnt += 1
        if n <= cnt <= m:
            sum_val += i
        elif cnt > m:
            break

print(sum_val)