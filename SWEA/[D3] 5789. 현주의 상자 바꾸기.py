for TC in range(1, int(input())+1): # 테스트 케이스
    N, Q = map(int, input().split()) # 전체 상자의 수 N, 작업할 횟수 Q
    boxes = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split()) # L에서 R까지
        for j in range(L-1, R): # L에서 R까지
            boxes[j] = i # i로 바꾸기
    
    # 제출을 위한 형식으로 만들기
    result = ''
    for box in boxes:
        result += str(box) + ' '
    result = result[0:-1] # 마지막 공백 없애주기
    print(f'#{TC} {result}')