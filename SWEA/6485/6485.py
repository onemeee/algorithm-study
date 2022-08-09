for TC in range(1, int(input())+1):
    busses = [] # N개의 버스노선이 담길 리스트 생성
    for i in range(int(input())): # N 개의 노선
        bus_line = list(map(int, input().split())) # A - B까지의 노선
        busses.append(bus_line)
    
    P = int(input())
    bus_stop = [0] * P # P 개의 버스정류장
    for j in range(P):
        C = int(input()) # j 번째 버스 정류장 
        for bus in busses: # 각 노선을 살펴볼 때
            if bus[0] <= C <= bus[1]: # 정류장이 노선 사이에 존재하면
                bus_stop[j] += 1 # j 번째 정류장 + 1
    # 출력을 위한 형식 정리
    result = ''
    for num in bus_stop:
        result += f'{num} '
    result = result[:-1] # 마지막 공백 지우기
    print(f'#{TC} {result}')