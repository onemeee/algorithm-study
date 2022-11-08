import sys
input = sys.stdin.readline

nums = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    nums.append((a, b))
nums.sort(key=lambda x:(x[1], x[0]))
for c, d in nums:
    print(c, d)