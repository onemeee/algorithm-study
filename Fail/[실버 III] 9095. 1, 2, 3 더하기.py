def fibo_trans(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return fibo_trans(n-1) + fibo_trans(n-2) + fibo_trans(n-3)

for _ in range(int(input())):
    print(fibo_trans(int(input())))