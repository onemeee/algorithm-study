for tc in range(1, int(input())+1):
    stack = []
    infos = list(input().split())
    for info in infos:
        if info.isdecimal():
            stack.append(int(info))
        elif info == '.':
            if len(stack) == 1:
                result = stack[-1]
            else:
                result = 'error'
        else:
            if len(stack) < 2:
                result = 'error'
                break
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if info == '+':
                    val = val1 + val2
                elif info == '-':
                    val = val2 - val1
                elif info == '*':
                    val = val2 * val1
                elif info == '/':
                    val = val2 // val1
                stack.append(val)
    print(f'#{tc} {result}')