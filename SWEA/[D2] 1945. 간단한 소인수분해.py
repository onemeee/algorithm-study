def Factorization(target, num): # 하나의 값에 대하여 소인수 분해
    count = 0
    while target%num == 0:
        count += 1
        target //= num
    return count

for TC in range(1, int(input())+1): # 테스트 케이스
    N = int(input()) # 인수분해 할 값
    a = Factorization(N, 2)
    b = Factorization(N, 3)
    c = Factorization(N, 5)
    d = Factorization(N, 7)
    e = Factorization(N, 11)
    print(f'#{TC} {a} {b} {c} {d} {e}')