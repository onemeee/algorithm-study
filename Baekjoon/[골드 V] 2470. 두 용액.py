import sys

input = sys.stdin.readline

def find():
    n = int(input())

    sols = sorted(list(map(int, input().rstrip().split())))

    if sols[0] >= 0:
        print(sols[0], sols[1])
        return

    elif sols[-1] <= 0:
        print(sols[-2], sols[-1])
        return

    left, right = 0, n-1
    ans_l, ans_r = 0, n-1
    gap = float('inf')

    while left != right:
        tmp = sols[left] + sols[right]
        if abs(tmp) < gap:
            gap = abs(tmp)
            ans_l, ans_r = left, right
        if tmp == 0:
            print(sols[ans_l], sols[ans_r])
            return 
        elif tmp > 0:
            right -= 1
        else:
            left += 1
    
    print(sols[ans_l], sols[ans_r])
    return

find()