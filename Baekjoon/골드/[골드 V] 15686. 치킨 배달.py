import sys
input = sys.stdin.readline

# 조합 구현하는 dfs
def dfs(elements, start, m):
    global k
    if m == 0:
        results.append(elements[:])
        return
    for i in range(start, k):
        elements.append(i)
        dfs(elements, i+1, m-1)
        elements.pop()

# 거리 계산하기
def calc(i, j):
    min_val = float('INF')
    for idx in result:
        ti, tj = stores[idx]
        tmp = abs(i-ti) + abs(j-tj)
        min_val = min(min_val, tmp)
    return min_val

n, m = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)]
homes = []
stores = []
ans = float('INF')
# 집, 가게 좌표 찾기
for i in range(n):
    for j in range(n):
        if infos[i][j] == 1:
            homes.append((i, j))
        elif infos[i][j] == 2:
            stores.append((i, j))
# 가게의 수
k = len(stores)
# 0~k-1 중에 m개의 번호 뽑기(조합)
results = []
dfs([], 0, m)
# 거리 계산
for result in results:
    tmp_ans = 0
    for ci, cj in homes:
        tmp_ans += calc(ci, cj)
    ans = min(ans, tmp_ans)
print(ans)