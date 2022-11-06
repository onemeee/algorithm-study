# 음수해결하기
import sys
input = sys.stdin.readline

def cal(nums):
    m = len(nums)
    print(sum(nums)//m)
    nums.sort()
    print(nums[m//2])
    check = [0] * (nums[-1]+1)
    for num in nums:
        check[num] += 1
    max_val = max(check)
    max_idx = check.index(max(check))
    for k in range(max_idx+1, len(check)):
        if check[k] == max_val:
            print(k)
            break
    else:
        print(max_idx)
    print(nums[-1]-nums[0])

nums = [int(input()) for _ in range(int(input()))]
cal(nums)