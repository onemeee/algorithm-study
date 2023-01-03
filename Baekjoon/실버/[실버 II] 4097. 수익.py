import sys

input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    result = float("-inf")
    rev = [0] * (n+1)

    for i in range(1, n+1):
        p = int(input())
        rev[i] = max(rev[i-1]+p, p)
        result = max(rev[i], result)
    
    print(result)