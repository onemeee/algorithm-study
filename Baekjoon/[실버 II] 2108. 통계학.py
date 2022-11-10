# 음수해결하기
import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
# 산술평균
print(round(sum(nums)/n))

# 중앙값
nums.sort()
print(nums[n//2])

# 최빈값
check = {}
for num in nums:
    if num in check:
        check[num] += 1
    else:
        check[num] = 1

max_val = max(check.values())

keys = []
for key, val in check.items():
    if val == max_val:
        keys.append(key)

if len(keys) >=2:
    keys.sort()
    print(keys[1])
else:
    print(keys[0])

# 범위
print(nums[-1]-nums[0])