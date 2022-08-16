for TC in range(1, int(input())+1):
    N = int(input())
    prices = list(map(int, input().split()))
    buy_num = [0] * N
    max_val = prices[-1]
    max_idx = N-1
    
    for i in range(N-2, -1, -1): # 마지막 날은 어쩌피 못삼
        if max_val < prices[i]:
            max_val = prices[i]
            max_idx = i
        else:
            buy_num[i] -= 1
            buy_num[max_idx] += 1

    total = 0
    for j in range(N):
        total += prices[j] * buy_num[j]

    print(f'#{TC} {total}')