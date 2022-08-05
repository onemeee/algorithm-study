for i in range(int(input())):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    max_val = 0
    min_val = sum(num_list)
    for j in range(N-M+1):
        tmp = sum(num_list[j:j+M])
        if tmp < min_val:
            min_val = tmp
        if tmp > max_val:
            max_val = tmp
    print(f'#{i+1} {max_val-min_val}')