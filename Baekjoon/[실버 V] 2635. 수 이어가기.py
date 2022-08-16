num_1st = int(input())
length = 0
for num_2nd in range(num_1st//2, num_1st + 1):
    len_list = []
    len_list.append(num_1st)
    len_list.append(num_2nd)
    while len_list[-1] >= 0:
        len_list.append(len_list[-2] - len_list[-1])
    len_list.pop() # 마지막 요소 제거(음수)
    if len(len_list) > length:
        length = len(len_list)
        len_result = len_list.copy()
print(length)
print(' '.join(map(str, len_result)))