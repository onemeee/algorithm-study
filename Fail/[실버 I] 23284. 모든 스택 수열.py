n = int(input())

result = []
def stack_result(i, arr, stack):
    global n
    if i == n+1:
        result.append(arr)
        return
    stack.append(i)
    stack_result(i+1, arr, stack)
    for j in range(len(stack)):
        arr.append(stack.pop())
        stack_result(i+1, arr, stack)

stack_result(1, [], [])
print(result)