import sys
input = sys.stdin.readline
product = 1
num_list = [0] * 10
for _ in range(3):
    product *= int(input())
while product:
    num_list[product%10] += 1
    product //= 10
for num in num_list:
    print(num)