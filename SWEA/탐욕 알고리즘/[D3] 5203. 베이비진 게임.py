def check(user):
    global p1_val
    global p2_val
    if len(user) >= 3:
        for i in set(user):
            # triplet
            tmp = user.count(i)
            if tmp >= 3:
                if user == p1:
                    p1_val = True
                else:
                    p2_val = True
                return
            # run
            tmp2 = 0
            for j in range(3):
                if i + j in user:
                    tmp2 += 1
            if tmp2 == 3:
                if user == p1:
                    p1_val = True
                else:
                    p2_val = True
                return
        return
    return

for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    p1 = []
    p1_val = False
    p2 = []
    p2_val = False
    result = 0
    for i in range(12):
        if i%2:
            p2.append(cards[i])
            check(p2)
        else:
            p1.append(cards[i])
            check(p1)
        if p1_val:
            result = 1
            break
        elif p2_val:
            result = 2
            break
    print(f'#{tc} {result}')