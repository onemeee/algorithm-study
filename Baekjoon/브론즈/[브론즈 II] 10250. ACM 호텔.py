import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h, w, n = map(int, input().split())
    cnt = 0
    floor = 0
    room = 1
    while cnt < n:
        floor += 1
        cnt += 1
        if floor == h+1:
            room += 1
            floor = 1
    if room < 10:
        print(f'{floor}0{room}')
    else:
        print(f'{floor}{room}')