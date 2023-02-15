# 좌, 우, 상, 하 
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

loc = list(input())
# 현재 ㅁ열, 행
ci, cj = ord(loc[0])-97, int(loc[1])-1
result = 0

# 4가지 방향에 대해 탐색
for k in range(4):
    # 수평 혹은 수직으로 2번 이동
    ni, nj = ci + di[k]*2, cj + dj[k]*2
    # 수직 혹은 수평으로 1번 이동
    if k == 0 or k == 1: # 수평인 경우
        # 수직으로 이동
        l = 2
    else: # 수직인 경우
        l = 0
    for m in range(l, l+2):
        ni += di[m]
        nj += dj[m]
        if 0 <= ni <= 7 and 0 <= nj <= 7:
            result += 1

print(result)