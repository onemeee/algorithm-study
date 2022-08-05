for i in range(int(input())):
    n = int(input())
    num_list = list(map(int, input().split()))
    result = max(num_list) - min(num_list)
    print(f'#{i+1} {result}')