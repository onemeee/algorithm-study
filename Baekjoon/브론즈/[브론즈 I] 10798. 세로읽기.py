words = [list(input()) for _ in range(5)]

col = 0
ans = ''
while True:
    no = 0
    for i in range(5):
        if col < len(words[i]):
            ans += words[i][col]
            continue
        no += 1
    col += 1
    if no == 5:
        break

print(ans)
