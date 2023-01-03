import sys
sys.setrecursionlimit(10**9)

def game(visited, x, y, move):
    global max_move
    # 시작 지점
    visited[x][y] = move
    max_move = max(max_move, move)

    for i in range(4):
        if max_move == -1:
            return
        nx = x + dx[i]*int(board[x][y])
        ny = y + dy[i]*int(board[x][y])
        nextmove = move + 1
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 'H':
            if check[nx][ny]:
                max_move = -1
                return
            elif visited[nx][ny] == 0 or visited[nx][ny] < nextmove:
                check[nx][ny] = 1
                game(visited, nx, ny, nextmove)
                check[nx][ny] = 0


N, M = map(int, input().split())
# 보드 상태 업데이트
board = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
check = [[0] * M for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
max_move = 0
game(visited, 0, 0, 1)
print(max_move)