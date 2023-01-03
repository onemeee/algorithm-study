n, m = map(int, input().split())
cards = sorted(list(map(int, input().split())))
result = 0
for i in range(n-1):
    left = i+1
    right = n-1
    while True:
        if left <= i:
            break
        if right >= n:
            break
        if left == right:
            break
        val = cards[i] + cards[left] + cards[right]
        if val < m:
            result = max(result, val)
            left += 1
        elif val == m:
            result = val
            break
        else:
            right -= 1
print(result)