def solution(arr):
    ans = [arr[0]]
    for num in arr:
        if ans[-1] != num:
            ans.append(num)
    return ans