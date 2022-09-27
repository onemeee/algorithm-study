def perm(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in perm(arr[:i] + arr[i+1:], r-1):
                yield [arr[i]] + next

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    order = [i for i in range(n)]
    min_val = 500
    for next in perm(order, n):
        tmp_val = 0
        for i in range(n):
            tmp_val += arr[i][next[i]]
            if tmp_val > min_val:
                break
        min_val = min(min_val, tmp_val)
    print(f'#{tc} {min_val}')