import sys 
input = sys.stdin.readline

def permu(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]]
        else:
            for next in permu(arr[:i] + arr[i+1:], k-1):
                yield [arr[i]] + next

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
result = set()
for next in permu(nums, m):
    if tuple(next) not in result:
        result.add(tuple(next))
        print(*next)