from collections import deque
for tc in range(1, int(input())+1):
    n = int(input())
    infos = [list(map(int, input().split())) for _ in range(n)]
    power = 0
    cracks = []
    for i in range(n-1):
        x, y, dire, k = infos[i][0], infos[i][1], infos[i][2], infos[i][3]
        for j in range(i+1, n):
            tmp_x, tmp_y, tmp_dire, tmp_k = infos[j][0], infos[j][1], infos[j][2], infos[j][3]
            # 좌우 충돌
            if y == tmp_y:
                if dire == 2 and tmp_dire == 3:
                    if x < tmp_x:
                        continue
                elif dire == 3 and tmp_dire == 2:
                    if x > tmp_x:
                        continue
                else:
                    continue
                cracks.append((abs(x-tmp_x)/2, i, j))
            # 상하 충돌
            if x == tmp_x:
                if dire == 0 and tmp_dire == 1:
                    if y > tmp_y:
                        continue
                elif dire == 1 and tmp_dire == 0:
                    if y < tmp_y:
                        continue
                else:
                    continue
                cracks.append((abs(y-tmp_y)/2, i, j))
            # 가로, 세로 충돌
            if dire == 0:
                if tmp_dire == 2: 
                    if x >= tmp_x or y >= tmp_y:
                        continue
                elif tmp_dire == 3:
                    if x <= tmp_x or y >= tmp_y:
                        continue
                else:
                    continue
            elif dire == 1:
                if tmp_dire == 2:
                    if x >= tmp_x or y <= tmp_y:
                        continue
                elif tmp_dire == 3:
                    if x <= tmp_x or y <= tmp_y:
                        continue
                else:
                    continue
            elif dire == 2:
                if tmp_dire == 0:
                    if tmp_x >= x or tmp_y >= y:
                        continue
                elif tmp_dire == 1:
                    if tmp_x >= x or tmp_y <= y:
                        continue
                else:
                    continue
            elif dire == 3:
                if tmp_dire == 0:
                    if tmp_x <= x or tmp_y >= y:
                        continue
                elif tmp_dire == 1:
                    if tmp_x <= x or tmp_y <= y:
                        continue
                else:
                    continue
            if abs(x-tmp_x) == abs(y-tmp_y):
                    cracks.append((abs(x-tmp_x), i, j))
    cracks.sort()
    vanish = {}
    for crack in cracks:
        i = crack[1]
        j = crack[2]
        if i in vanish and j in vanish:
            continue
        elif i in vanish:
            if crack[0] == vanish[i]:
                power += infos[j][3]
                vanish[j] = crack[0]
        elif j in vanish:
            if crack[0] == vanish[j]:
                power += infos[i][3]
                vanish[i] = crack[0]
        else:
            power += infos[i][3]
            power += infos[j][3]
            vanish[i] = crack[0]
            vanish[j] = crack[0]
    print(f'#{tc} {power}')
