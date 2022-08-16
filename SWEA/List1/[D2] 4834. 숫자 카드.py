for i in range(int(input())):
    count = {}
    N = int(input())
    num = input()
    num_list = list(map(int, num))
    for num in num_list:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    max_key = []
    max_val = 0
    for key, val in count.items():
        if val > max_val:
            max_val = val
            max_key.clear()
            max_key.append(key)
        elif val == max_val:
            max_key.append(key)
    real_key = max(max_key)
    print(f'#{i+1} {real_key} {count.get(real_key)}')
