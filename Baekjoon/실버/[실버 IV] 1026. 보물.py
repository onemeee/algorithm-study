N = int(input())
orders = []
re_A = [0] * N
A = list(map(int, input().split()))
B = list(map(int, input().split()))
tmp = B.copy()

for i in range(N):
    orders.append(tmp.index(max(tmp)))
    tmp[orders[-1]] = -1

A.sort()

for i in range(N):
    re_A[orders[i]] = A[i]

sum = 0
for i in range(N):
    sum += re_A[i] * B[i]

print(sum) 