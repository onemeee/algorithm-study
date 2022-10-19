import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    apart = [[0] * (n) for _ in range(k+1)]
    for i in range(n):
        apart[0][i] = i+1
    for l in range(1, k+1):
        for m in range(n):
            for j in range(m+1):
                apart[l][m] += apart[l-1][j]
    print(apart[k][n-1]) 