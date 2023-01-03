n = int(input())
num = 0
while True:
    num += 1
    if num > n:
        print(0)
        break
    ans = num
    for i in str(num):
        ans += int(i)
    if ans == n:
        print(num)
        break
    