n = int(input())

def change(arr, i):
    if arr[i] == '0':
        arr[i] = '1'
    else:
        arr[i] = '0'

origin_ori = list(input())
origin_copy = origin_ori.copy()
change(origin_copy, 0)
change(origin_copy, 1)
target = list(input())
ans = []



for i in range(2):
    tmp = 0
    if i == 0:
        origin = origin_ori
    else:
        tmp += 1
        origin = origin_copy

    for i in range(1, n):
        if origin[i-1] != target[i-1]:
            tmp += 1
            change(origin, i-1)
            change(origin, i)
            if i == n-1:
                break
            change(origin, i+1)

    if ''.join(origin) == ''.join(target):
        ans.append(tmp)

if ans:
    print(min(ans))
else:
    print(-1)