for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    candys = [n//m]*m
    for i in range(n-(n//m)*m):
        candys[i] += 1
    result = 1
    for candy in candys:
        result *= candy
    print(f'#{tc} {result}')