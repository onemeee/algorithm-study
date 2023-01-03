import sys
input = sys.stdin.readline

def find(n):
    if n == 1:
        return False
    for i in range(2, n):
        if not n%i:
            return False
    return True

n = int(input())
num_list = list(map(int, input().split()))

cnt = 0
for num in num_list:
    result = find(num)
    if result:
        cnt += 1
print(cnt)