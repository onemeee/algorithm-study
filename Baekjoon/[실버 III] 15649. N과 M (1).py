def backtracking():
    if len(result) == m:
        print(*result)
        return
    for num in nums:
        if num not in result:
            result.append(num)
            backtracking()
            result.pop()

result= []
n, m = map(int, input().split())
nums = [i+1 for i in range(n)]
backtracking()
