string = input()
stack1 = []
stack2 = []
flag = False

for s in string:
    if s =='<':
        if stack2:
            stack1 += stack2[::-1]
            stack2.clear()
        flag = True
        stack1.append(s)
    elif s == '>':
        flag = False
        stack1.append(s)
    else:
        if flag:
            stack1.append(s)
        else:
            if s == ' ':
                stack1 += stack2[::-1]
                stack2.clear()
                stack1.append(s)
            else:
                stack2.append(s)

if stack2:
    stack1 += stack2[::-1]
print(''.join(stack1))
