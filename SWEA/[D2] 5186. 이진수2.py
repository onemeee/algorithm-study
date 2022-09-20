for tc in range(1, int(input())+1):
    info = float(input())
    result = ''
    for i in range(1, 13):
        if info >= 2 ** (-i):
            info -= 2 ** (-i)
            result += str(1)
        else:
            result += str(0)
        if info == 0:
            break
    if info:
        result = 'overflow'
    print(f'#{tc} {result}')