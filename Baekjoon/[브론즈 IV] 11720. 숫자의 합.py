n = int(input())
nums = int(input())
sum_num = 0
while nums:
    sum_num += nums%10
    nums //= 10
print(sum_num)