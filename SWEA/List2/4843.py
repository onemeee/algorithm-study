for i in range(int(input())):
    total_num = int(input())
    num_list = list(map(int, input().split()))
    sort_list = sorted(num_list)
    rev_list = sorted(num_list, reverse=True)
    num_sort = [0]*total_num
    for j in range(total_num//2):
        num_sort[j*2] = rev_list[j]
        num_sort[j*2+1] = sort_list[j]
    if total_num%2:
        num_sort[-1] = rev_list[total_num//2]
    result = ' '.join(map(str, num_sort[0:10]))
    print(f'#{i+1} {result}')