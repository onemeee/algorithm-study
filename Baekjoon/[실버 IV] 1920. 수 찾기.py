# in 시간복잡도 n
# sort 시간복잡도 nlogn

def binary(list, target, num):
    l = 0
    r = num-1

    while True:
        if l <= r:
            mid = (l+r)//2
            if list[mid] == target:
                print(1)
                break
            elif list[mid] > target:
                r = mid - 1
            elif list[mid] < target:
                l = mid + 1
        else:
            print(0)
            break
        
N = int(input())
num_list = sorted(list(map(int, input().split())))
M = int(input())
num_list2 = list(map(int, input().split()))
for target_num in num_list2:
    binary(num_list, target_num, N)