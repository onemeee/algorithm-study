for TC in range(1, int(input())+1):
    infos = input()
    pipe_list = [0] * len(infos)
    laser_list = [0] * len(infos)
    pipe_num = 0

    for i in range(len(infos)):
        if infos[i] == '(':
            if infos[i+1] == ')':
                laser_list[i] += 1
                pipe_list[i] = pipe_num
            else:
                pipe_num += 1
                pipe_list[i] = pipe_num
        elif infos[i] == ')':
            if infos[i-1] == ')':
                pipe_num -= 1
                pipe_list[i] = pipe_num
            else:
                pipe_list[i] = pipe_num

    cnt = 0
    for j in range(len(pipe_list)):
        if laser_list[j] == 1:
            cnt += pipe_list[j]
        if j != 0 and pipe_list[j] < pipe_list[j-1]:
            cnt += 1
    print(f'#{TC} {cnt}')