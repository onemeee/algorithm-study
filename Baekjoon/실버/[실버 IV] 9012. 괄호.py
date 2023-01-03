for TC in range(1, int(input())+1):
    stack = [] # ()를 담을 stack
    flag = False
    
    check = input()
    for i in check:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                flag = True
                break
    if flag:
        result = 'NO'
    else:
        if len(stack) == 0:
            result = 'YES'
        else:
            result = 'NO'
    print(result)