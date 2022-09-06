def nums_list(arr, m):
    for i in range(len(arr)):
        if m == 1:
            yield [arr[i]]
        else:
            for next in nums_list(arr[i+1:],m-1):
                yield [arr[i]] + next

n, m = map(int, input().split())
arr = [i for i in range(1,n+1)]
for nums in nums_list(arr, m):
    print(*nums)