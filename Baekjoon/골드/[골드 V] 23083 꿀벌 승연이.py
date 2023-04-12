def hole():
    for _ in range(k):
        x, y = map(int, input().split())
        honey[x][y] = 0

def find(i, j):
    if i < 1 or j < 1 or i > n or j > m:
        honey[i][j] = 0
        return honey[i][j]
    if honey[i][j] != -1:
        return honey[i][j]
    if j % 2:
        cnt = find(i-1, j-1) + find(i, j-1) + find(i-1, j)
        honey[i][j] = cnt % (10**9 + 7)
        return honey[i][j]
    else:
        cnt = find(i+1, j-1) + find(i, j-1) + find(i-1, j)
        honey[i][j] = cnt % (10**9 + 7)
        return honey[i][j]
    
n, m = map(int, input().split())
k = int(input())
honey = [[-1] * (m+1) for _ in range(n+2)]
honey[1][1] = 1
hole()
print(find(n, m))