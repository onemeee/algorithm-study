# 후위표기식 구현
def postfix(formula):
    anw = '' # 표기식을 담을 문자열
    stack = [] # 연산자를 담을 스택
    for info in formula:
        # 피연산자
        if info.isdecimal():
            anw += info
        else:
            if stack:
                if info == '*':
                    while stack:
                        if stack[-1] == '*':
                            anw += stack.pop()
                        else:
                            break
                    stack.append(info)
                elif info == '+':
                    if stack[-1] == '(':
                        stack.append(info)
                    else:
                        while stack:
                            if stack[-1] != '(':
                                anw += stack.pop()
                            else:
                                break
                        stack.append(info)
                elif info == '(':
                    stack.append(info)
                elif info == ')':
                    while True:
                        if stack[-1] == '(':
                            break
                        else:
                            anw += stack.pop()
                    stack.pop()
            else:
                stack.append(info)
    if stack:
        while stack:
            anw += stack.pop()
    return anw

# 계산기 구현
def calc(formula):
    stack = [] # 숫자 담을 스택
    for info in formula:
        if info.isdecimal():
            stack.append(int(info))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if info == '+':
                val = val1 + val2
            else:
                val = val1 * val2
            stack.append(val)
    return stack[-1]

for tc in range(1, 11):
    N = int(input())
    infos = input()
    anw = postfix(infos)
    result = calc(anw)
    print(f'#{tc} {result}')