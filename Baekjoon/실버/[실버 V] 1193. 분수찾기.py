x = int(input())
arr = [0]


def find(x):
    n = 1
    while True:
        val1 = arr[-1]
        val2 = val1 + n
        if val1 < x <= val2:
            break
        arr.append(val2)
        n += 1
    return (n, x-val1-1)


n, move = find(x)

# 행부터
if n % 2:
    i = n
    j = 1
    for _ in range(move):
        i -= 1
        j += 1

# 열부터
else:
    j = n
    i = 1
    for _ in range(move):
        j -= 1
        i += 1

print(f'{i}/{j}')
