from collections import deque

n, k = map(int, input().split())
permu = []
num_list = deque(range(1, n+1))

for _ in range(n):
    num_list.rotate(-1*k)
    permu.append(num_list.pop())

print('<', end='')
print(*permu, sep=", ", end='')
print('>')