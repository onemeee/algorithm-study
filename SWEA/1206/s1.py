for TC in range(1, 11): # 테스트 케이스 10가지
    list_len = int(input())
    floors = list(map(int, input().split())) # 각 건물의 층 수 list에 넣기
    view = 0 # 조망권 확보된 가구 수
    for idx in range(len(floors)):
        if idx > 1 and idx < len(floors)-2: # 앞뒤로 2가지씩 비교 가능한 구간
            max_floor = max(floors[idx-1], floors[idx-2], floors[idx+1], floors[idx+2]) # 앞 뒤 건물 중 가장 높은 건물 층 수 찾기
            if floors[idx]> max_floor: # max_floor보다 커야 조망권이 존재하므로
                view += floors[idx] - max_floor # 현재 건물에서 조망권을 확보한 가구 추가
    print(f'#{TC} {view}')