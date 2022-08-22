for tc in range(1, 11):
    N = int(input())
    infos = input()
    stack = []
    anw = ''
    for info in infos:
        if info.isdecimal(): #int형 변환이 가능한지 check
            anw += info
        else:
            if info == '(':
                stack.append(info)
            elif info == ')':
                while stack and stack[-1] != '(':
                    anw += stack.pop()
            elif info == '+':
                while stack and stack[-1] != '(':
                    anw 
            elif info == '*':
                while stack and stack[-1] == '*':
                    anw += stack.pop()
    print(f'{tc}')