import sys
input = sys.stdin.readline

n = int(input())
nums = [0] * 10001
for _ in range(n):
    k = int(input())
    nums[k] += 1
for k in range(10001):
    for _ in range(nums[k]):
        print(k)