import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
k = 1
ans = 0

def bfs(arr, i, j):
    dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    que = deque()
    que.append((i, j))
    visited[i][j] = 1
    while que:
        ci, cj = que.popleft()
        arr[ci][cj] = 1

        for ki, kj in dires:
            ni, nj = ci + ki, cj + kj

            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                que.append((ni, nj))
                visited[ni][nj] = 1




while k <= 100:
    total = n ** 2
    visited = [[0] * n for _ in range(n)]
    tmp_cnt = 0

    # 잠기는 영역 체크
    for i in range(n):
        for j in range(n):
            if maps[i][j] <= k:
                visited[i][j] = 1
                total -= 1
    
    # 다 잠겨서 안전 영역이 존재하지 않음
    if total == 0:
        break

    # 안전영역 개수 확인
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(visited, i, j)
                tmp_cnt += 1

    # 최댓값 찾기
    ans = max(ans, tmp_cnt)

    # 높이 증가
    k += 1

if ans == 0:
    ans = 1
print(ans)