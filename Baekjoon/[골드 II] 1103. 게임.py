def game(visited):
    pass

N, M = map(int, input().split())
board = []
visited = []
# 보드 상태 업데이트
for _ in range(N):
    board.append(list(input()))
    visited.append([0] * M)