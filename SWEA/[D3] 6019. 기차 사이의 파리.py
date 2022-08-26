for tc in range(1, int(input())+1):
    d, a, b, f = map(int, input().split())
    # 기차가 충돌하기까지 걸린 시간
    time = d/(a+b)
    print(f'#{tc} {f*time}')