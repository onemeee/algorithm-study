stack = [] # 연산자를 담을 stack
result = '' # 후위표기식 결과
for info in input():
    if info == '*' or info == '/':
        if stack:
            while stack:
                if stack[-1] == '*' or stack[-1] == '/':
                    result += stack.pop()
                else:
                    break
        stack.append(info)
    elif info == '+' or info == '-':
        if stack:
            while stack:
                if stack[-1] != '(':
                    result += stack.pop()
                else:
                    break
        stack.append(info)
    elif info == '(':
        stack.append(info)
    elif info == ')':
        while stack[-1] != '(':
            result += stack.pop()
        stack.pop() # '(' 제거
    else:
        result += info
while stack:
    result += stack.pop()

print(result)
