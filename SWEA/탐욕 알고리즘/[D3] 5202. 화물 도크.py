for tc in range(1, int(input())+1):
    n = int(input())
    times = [list(map(int, input().split())) for _ in range(n)]
    times.sort(key = lambda x: x[1])
    end = 0
    cnt = 0
    for time in times:
        if time[0] >= end:
            cnt += 1
            end = time[1]
    print(f'#{tc} {cnt}')