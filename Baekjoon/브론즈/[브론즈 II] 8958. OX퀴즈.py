for _ in range(int(input())):
    info = input()
    score = 0
    tmp = 0
    for i in range(len(info)):
        if info[i] == 'O':
            tmp += 1
            score += tmp
        else:
            tmp = 0
    print(score)