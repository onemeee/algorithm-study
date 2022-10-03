import sys
input = sys.stdin.readline

def combi(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]] 
        else:
            for next in combi(arr[i+1:], k-1):
                yield [arr[i]] + next
n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]
min_val = 100 * n
nums = [i for i in range(1, n+1)]
for arr in combi(nums, n//2):
    arr2 = []
    for i in range(1, n+1):
        if i not in arr:
            arr2.append(i)
    sum_val1 = 0
    sum_val2 = 0
    for l in range(n//2-1):
        for m in range(l+1, n//2):
            sum_val1 += infos[arr[l]-1][arr[m]-1]
            sum_val1 += infos[arr[m]-1][arr[l]-1]
            sum_val2 += infos[arr2[l]-1][arr2[m]-1]
            sum_val2 += infos[arr2[m]-1][arr2[l]-1]
    min_val = min(min_val, abs(sum_val1 - sum_val2))
print(min_val)