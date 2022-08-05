for i in range(int(input())):
    move_num, target, charge_num = map(int, input().split())
    charge_list = list(map(int, input().split()))
    charge_list.append(target)
    count = 0
    charge = 0
    move = move_num
    while True:
        count += 1
        move -= 1
        if count == target and move>=0:
            break
        if count in charge_list and move >= 0:
            if charge_list[charge_list.index(count)] + move < charge_list[charge_list.index(count) + 1]:
                print(charge_list[charge_list.index(count)])
                charge += 1
                move = move_num
        elif move < 0:
            print(f'#{i+1} 0')
            break