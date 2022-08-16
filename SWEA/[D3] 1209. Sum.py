# 합 구하기 함수
def mysum(num_list):
    sum = 0
    for num in num_list:
        sum += num
    return sum

# 최댓값 구하기 함수
def mymax(a,b):
    if a > b:
        return a
    return b

for TC in range(1, 11):
    grid = []
    max_row = 0
    N = input()

    # 행들 내에서 최댓값 찾기
    for _ in range(100):
        nums = list(map(int, input().split()))
        val = mysum(nums)
        # 최댓값 업데이트
        max_row = mymax(val, max_row)
        grid.append(nums)    

    # 열의 최댓값 찾기
    max_col = 0
    reverse = [[grid[row][col] for row in range(100)] for col in range(100)]
    for col in reverse:
        val = mysum(col)
        max_col = mymax(max_col, val)

    # 대각선 최댓값 찾기
    delta = [[1,1], [1,-1]]
    dia1 = 0
    dia2 = 0
    dia1_x, dia1_y = 0, 0
    dia2_x, dia2_y = 0, 99
    for _ in range(100):
        dia1 += grid[dia1_x][dia1_y]
        dia2 += grid[dia2_x][dia2_y]
        # 위치 옮기기
        dia1_x += delta[0][0]
        dia1_y += delta[0][1]
        dia2_x += delta[1][0]
        dia2_y += delta[1][1]
    max_dia = mymax(dia1, dia2)
    
    # 세개의 값 중 최대 비교
    tmp_max = mymax(max_row, max_col)
    max_val = mymax(max_dia, tmp_max)
    print(f'#{TC} {max_val}')