import sys
input = sys.stdin.readline

# 카운팅 정렬 구현
n = int(input())
nums = [int(input()) for _ in range(n)]
m = max(nums)
min_val = min(nums)
k = 0
if min_val < 0:
    k = -min_val
arr = [0] * (m+k+1)
for num in nums:
    arr[num+k] += 1
result = []
for i in range(len(arr)):
    for j in range(arr[i]):
        result.append(i-k)

for re in result:
    print(re)