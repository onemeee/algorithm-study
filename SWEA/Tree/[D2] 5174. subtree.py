def count(n):
    global cnt
    if n:
        cnt += 1
        count(left[n])
        count(right[n])

for tc in range(1, int(input())+1):
    E, n = map(int, input().split())
    left = [0] * (E+2)
    right = [0] * (E+2)
    cnt = 0
    infos = list(map(int, input().split()))
    for i in range(E):
        idx, num = infos[2*i], infos[2*i+1]
        if not left[idx]:
            left[idx] = num
        else:
            right[idx] = num
    
    count(n)
    print(f'#{tc} {cnt}')
    
