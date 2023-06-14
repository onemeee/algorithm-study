import sys
input = sys.stdin.readline

n = int(input())
stack = [0]
num = 1
for _ in range(1, n+1):
    val = int(input())
    if num == val:
        print('+')
        print('-')
    elif num < val:
        stack.append(num)
        num += 1
