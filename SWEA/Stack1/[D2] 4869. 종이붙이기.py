def fibo_trans(n):
    if n == 0:
        return 1
    elif n == 1:
        return 3
    else:
        return fibo_trans(n-2) * 2 + fibo_trans(n-1)

for TC in range(1, int(input())+1):
    n = int(input())//10 - 1
    result = fibo_trans(n)
    print(f'#{TC} {result}')