n = int(input())
infos = list(map(int, input().split()))
orders = [0] * n

for i in range(n):
    big = infos[i]
    for j in range(n):
        if orders[j] > i:
            big -= 1
        elif orders[j] == 0:
            if big <= 0:
                orders[j] = i+1
                break
            big -= 1

print(*orders)
