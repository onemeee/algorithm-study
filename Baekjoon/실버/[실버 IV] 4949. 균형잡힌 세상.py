while True:
    stack = [] # (), []을 담을 stack
    flag = False # 이미 결과가 0임을 알려주는 flag
    check = input()
    if check == '.':
        break
    for i in check:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = True
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = True
                break
        elif i == '.':
            break
    if flag:
        result = 'no'
    else:
        if len(stack) == 0:
            result = 'yes'
        else:
            result = 'no'
    print(result)