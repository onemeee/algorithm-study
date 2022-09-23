import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
length = 100001
tmp = nums[0]
i = j = 0

while True:
    if i > n-1:
        break
    if j < i:
        j += 1
        tmp += nums[j]
        continue
    if tmp >= s:
        length = min(length, j-i+1)
        i += 1
        tmp -= nums[i-1]
    else:
        j += 1
        if j > n-1:
            j -= 1
            i += 1
            tmp -= nums[i-1]
            continue
        tmp += nums[j]

if length == 100001:
    print(0)
else:
    print(length) 