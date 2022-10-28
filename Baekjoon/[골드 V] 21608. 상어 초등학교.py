import sys
input = sys.stdin.readline

def check(num, students):
    global n
    infos = []
    for i in range(n):
        for j in range(n):
            if not grid[i][j]:
                blank, like = 0, 0
                for dire in dires:
                    ni, nj = i+dire[0], j+dire[1]
                    if 0 <= ni < n and 0 <= nj < n:
                        if grid[ni][nj] in students:
                            like -= 1
                        elif not grid[ni][nj]:
                            blank -= 1
                        infos.append((like, blank, i, j))
    infos.sort()
    for info in infos:
        if not grid[info[2]][info[3]]:
            grid[info[2]][info[3]] = num
            break
    
def score():
    global n, ans
    for i in range(n):
        for j in range(n):
            num = grid[i][j]
            infos = info_dic[num]
            like = 0
            for dire in dires:
                ni, nj = i+dire[0], j+dire[1]
                if 0 <= ni < n and 0 <= nj < n:
                    if grid[ni][nj] in infos:
                        like += 1
            if like == 1:
                ans += 1
            elif like == 2:
                ans += 10
            elif like == 3:
                ans += 100
            elif like == 4:
                ans += 1000            



n = int(input())
grid = [[0] * n for _ in range(n)]
dires = [(-1, 0), (1, 0), (0, -1), (0, 1)]
info_dic = {}
ans = 0
for i in range(n**2):
    k, *L = map(int, input().strip().split())
    info_dic[k] = L
    if i == 0:
        grid[1][1] = k
    else:
        check(k, L)
score()
print(ans)