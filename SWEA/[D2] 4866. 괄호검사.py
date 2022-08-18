for TC in range(1, int(input())+1):
    stack = [] # (), []을 담을 stack
    flag = False # 이미 결과가 0임을 알려주는 flag
    check = input()
    for i in check:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = True
                break
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                flag = True
                break
    if flag:
        result = 0
    else:
        if len(stack) == 0:
            result = 1
        else:
            result = 0
    print(f'#{TC} {result}')