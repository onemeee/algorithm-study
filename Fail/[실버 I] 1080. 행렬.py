import sys
input = sys.stdin.readline

INF = 51 * 51

n, m = map(int, input().split())
a = [list(map(int, input().rstrip().split())) for _ in range(n)]
b = [list(map(int, input().rstrip().split())) for _ in range(n)]

min_val = INF

# 행렬 뒤집기
def change(arr, i, j):
    # 값 바꾸기
    val = arr[i][j]
    if val == 1:
        new_val = 0
    else:
        new_val = 1

    # 3x3 행렬 값 변경
    for ci in range(i, i+3):
        for cj in range(j, j+3):
            arr[ci][cj] = new_val

for i in range(n-3):
    for j in range(m-3):
        pass