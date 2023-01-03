n = int(input())
ans = 1
num = 1
tmp = 6
while True:
    if n <= num:
        print(ans)
        break
    ans += 1
    num += tmp
    tmp += 6
