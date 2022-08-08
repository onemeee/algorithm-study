def findc(find_num, total_num):
        count = 0
        l = 1
        r = total_num
        while True:
            count += 1
            c = (l+r)//2
            if c == find_num:
                return count
            elif c < find_num:
                l = c
            else:
                r = c
                
for TC in range(1, int(input())+1):
    total, findA, findB = map(int, input().split())
    a = findc(findA, total)
    b = findc(findB, total)
    if a > b:
        result = 'B'
    elif a < b:
        result = 'A'
    else:
        result = 0
    print(f'#{TC} {result}')