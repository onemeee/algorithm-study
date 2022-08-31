infos = input()
num_list = [0]
cnt_1 = 0
cnt_2 = 0
for i in range(len(infos)-1):
    if infos[i] == '(':
        if infos[i+1] == '(':
            cnt_1 += 1
    else:
        if infos[i] == ')':
            if infos[i+1] == ')':
                cnt_2 += 1
            else:
                if infos[i+1] == '(':
                    if cnt_2:
                        num_list.append(cnt_1*cnt_2 + num_list[-1])
                        cnt_2 = 0
if cnt_2:
    num_list.append(cnt_1*cnt_2 + num_list[-1])
print(num_list[-1]) 

            