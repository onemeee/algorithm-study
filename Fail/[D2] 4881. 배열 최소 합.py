def tracking(arr, num):
    if len(result) == n:
        vals.append(sum(result))
        return
    for i in range(len(arr[num])):
        result.append(arr[num][i])
        num += 1
        tracking(arr, num)
        result.pop()
        num -= 1

        
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []
    vals = []
    tracking(arr, 0)
    print(f'#{tc} {min(vals)}')