def changeswitch(list, index): # 스위치 바꾸는 함수 정의
    if list[index]:
        list[index] = 0
    else:
        list[index] = 1

N = int(input()) # 스위치의 개수
switch = list(map(int, input().split())) # 스위치 상태 입력
for _ in range(int(input())): # 학생수
    gender, num = map(int, input().split())
    if gender == 1: # 남자인 경우
        i = 1
        while True: # 입력 받은 숫자의 배수에 대하여 스위치 바꾸기
            idx = num * i
            if idx > len(switch): # list 범위를 벗어난 경우 탈출
                break
            changeswitch(switch, idx-1)
            i += 1
    else: # 여자인 경우
        changeswitch(switch, num-1) # 자기 자신 스위치 바꾸기
        l = num -2
        r = num
        while -1< l and r < len(switch): # 양 사이드 스위치 바꾸기
            if switch[l] == switch[r]:
                changeswitch(switch, l)
                changeswitch(switch, r)
                l -= 1
                r += 1
            else:
                break
# 프린트 형식 만들기
slice_idx = 0
while slice_idx <= len(switch) - 20:
    print(*switch[slice_idx:slice_idx+20])
    slice_idx += 20
print(*switch[slice_idx::])
