import sys
input = sys.stdin.readline
nums = [int(input()) for _ in range(9)]
max_idx = 0
max_num = nums[0]
for i, num in enumerate(nums):
    if num > max_num:
        max_num = num
        max_idx = i
print(max_num)
print(max_idx+1)
