import sys
input = sys.stdin.readline

def dfs(i, j):
    global n
    global num
    infos[i][j] = 0
    num += 1
    for dire in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i+dire[0], j+dire[1]
        if 0 <= ni < n and 0<= nj <n:
            if infos[ni][nj]:
                dfs(ni, nj)

n = int(input())
infos = [list(map(int, list(input().rstrip()))) for _ in range(n)]
total = 0
nums = []
for i in range(n):
    for j in range(n):
        if infos[i][j]:
            num = 0
            dfs(i, j)
            total += 1
            nums.append(num)
nums.sort()
print(total)
for num in nums:
    print(num)