def mymax(nums): # 리스트의 최댓값의 idx 찾는 함수 정의
    max_val = 0 # 최대값
    idx = -1 # 최댓값의 인덱스
    num_idx = -1 # 각 num의 인덱스
    for num in nums:
        num_idx += 1
        if num > max_val: # 인덱스 업데이트
            max_val = num
            idx = num_idx 
    return idx
            
def mymin(nums): # 리스트의 최솟값의 idx 찾는 함수 정의
    min_val = 101 # 최솟값
    idx = -1 # 최초값의 인덱스
    num_idx = -1 # 각 num의 인덱스
    for num in nums:
        num_idx += 1
        if num < min_val: # 인덱스 업데이트
            min_val = num
            idx = num_idx
    return idx

for TC in range(1, 11): # 테스트 케이스
    dump = int(input()) # 덤프 횟수
    boxes = list(map(int, input().split()))
    while dump > 0: # 덤프횟수 내에서
        dump -= 1
        max_idx = mymax(boxes) # 최대, 최소 idx 값 찾기
        min_idx = mymin(boxes)
        boxes[max_idx] -= 1  # 박스옮기기
        boxes[min_idx] += 1
        if boxes[max_idx] - boxes[min_idx] <= 1:
            break
    result = boxes[mymax(boxes)] - boxes[mymin(boxes)] # 최대, 최소 높이 차 구하기
    print(f'#{TC} {result}')