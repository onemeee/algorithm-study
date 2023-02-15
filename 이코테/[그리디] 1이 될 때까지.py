n, k = map(int, input().split())

val = 1
num = 0

# n에 가장 가까운 제곱수 구하기
while True:
    val *= k
    num += 1
    if val > n:
        num -= 1
        val //= k
        break

# 제곱 수 + k의 num 제급으로 나누어지지 않는 수
result = num + (n - val)
print(result)