# n: 재귀 반복, r: 행, c: 열, m: 시작 숫자
def find(n, r, c, m):
    k = 2**n
    if n == 0:
        print(m)
        return
    if r < k//2:
        if c < k//2:
            # 1 구역    
            find(n-1, r, c, m)
        else:
            # 2 구역
            find(n-1, r, c-k//2, m+(k//2)**2)
    else:
        if c < k//2:
            # 3 구역
            find(n-1, r-k//2, c, m+((k//2)**2)*2)
        else:
            # 4 구역
            find(n-1, r-k//2, c-k//2, m+((k//2)**2)*3)

n, r, c = map(int, input().split())
ans = find(n, r, c, 0)