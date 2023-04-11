import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
infos = []


for _ in range(k):
    cnt = 0
    x, r, c = map(int, input().rstrip().split())
    r, c = r-1, c-1

    # x의 위치
    ci, cj = x//n, (x % n)-1
    if cj < 0:
        cj += n
        ci -= 1

    # 누적된 이동 값
    for bi, bcol, bj, brow in infos:
        if ci == bi:
            cj += bcol
            cj %= n
        if cj == bj:
            ci += brow
            ci %= n

    # 이동 값 체크
    val1 = 0
    val2 = 0
    if ci <= r:
        val1 += abs(ci-r)
    else:
        val1 += n - abs(ci-r)
    if cj <= c:
        val2 += abs(cj-c)
    else:
        val2 += n - abs(cj-c)
    infos.append((ci, val2, c, val1))
    print(val1 + val2)
