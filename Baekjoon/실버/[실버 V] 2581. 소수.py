import sys
input = sys.stdin.readline
def find(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

n = int(input())
m = int(input())

sum_val = 0
cnt = 0
for num in range(n, m+1):
    result = find(num)
    if result:
        sum_val += num
        cnt += 1
        if cnt == 1:
            min_val = num
if sum_val == 0:
    print(-1)
else:
    print(sum_val)
    print(min_val)

