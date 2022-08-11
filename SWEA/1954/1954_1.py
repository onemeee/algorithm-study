for TC in range(1, int(input())+1):
    N = int(input())
    # 숫자가 들어갈 이차원 배열 생성
    snail = [[0 for col in range(N)] for row in range(N)]
    # 위치 조정을 위한 delta 배열 생성
    delta_row = [0, 1, 0, -1]
    delta_col = [1, 0, -1, 0]
    # 위치 관련 변수 생성
    now_row = 0
    now_col = -1
    # 방향 변화
    direction = 0
    change = [[0, N-1], [N-1, N-1], [N-1, 0]] # out of range 방지
    for num in range(1, N*N+1): # 숫자 작성
        now_row += delta_row[direction]
        now_col += delta_col[direction]
        if [now_row, now_col] in change: # out of range 되기 전에 위치 바꾸기
            direction += 1
            direction %= 4
        elif snail[now_row][now_col] != 0:
            # 되돌아가서
            now_row -= delta_row[direction]
            now_col -= delta_col[direction]
            # 위치바꾸고
            direction += 1
            direction %= 4
            # 다시 출발
            now_row += delta_row[direction]
            now_col += delta_col[direction]
        snail[now_row][now_col] = num
    # 프린트 작성
    print(f'#{TC}')
    for row in range(N):
        for col in range(N):
            print(snail[row][col], end=' ')
        print()