n, m, k = map(int, input().split())
nums = sorted(list(map(int, input().split())))
max_val, sec_val = nums[-1], nums[-2]
result = 0

# 반복 횟수 체크
check = 0

# m번 더해주기
for _ in range(m):
    if check == k:
        result += sec_val
        check = -1
    else:
        result += max_val
    check += 1
print(result)
