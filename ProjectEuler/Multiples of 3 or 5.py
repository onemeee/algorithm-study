def my_sum(val):
    global ans
    multiple = val
    while multiple < 1000:
        if multiple in check:
            multiple += val
            continue
        ans += multiple
        check.add(multiple)
        multiple += val


ans = 0
check = set()

my_sum(3)
my_sum(5)
print(ans)

# 새로운 아이디어
ans = 0

for i in range(1, 1000):
    if i % 3 == 0:
        ans += i
        continue
    if i % 5 == 0:
        ans += i
        continue

print(ans)

# 새로운 아이디어 - 수학 이용해보기
