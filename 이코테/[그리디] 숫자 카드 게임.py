n, m = map(int, input().split())

max_val = 0

# n번째 행까지 확인
for _ in range(n):
    # 숫자를 정렬해서 받음
    nums = sorted(list(map(int, input().split())))
    # 각 행의 최솟값들을 비교
    if nums[0] > max_val:
        max_val = nums[0]

print(max_val)