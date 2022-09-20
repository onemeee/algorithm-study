for tc in range(1, int(input())+1):
    result = ''
    n, infos = input().split()
    for info in infos:
        tmp = ''
        if info == 'A':
            info = 10
        elif info == 'B':
            info = 11
        elif info == 'C':
            info = 12
        elif info == 'D':
            info = 13  
        elif info == 'E':
            info = 14  
        elif info == 'F':
            info = 15
        info = int(info)    
        while info:
            tmp += str(info % 2)
            info //= 2
        while len(tmp) != 4:
            tmp += str(0)
        result += tmp[::-1]
    print(f'#{tc} {result}')