for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split()) # n명, m초, k개
    secs = list(map(int, input().split())) # n명이 도착하는 시각
    secs.sort()
    for i in range(len(secs)):
        num = secs[i]//m * k - i # 남은 붕어빵 개수
        if num > 0:
            result = "Possible"
        else:
            result = "Impossible"
            break 
    print(f'#{tc} {result}')