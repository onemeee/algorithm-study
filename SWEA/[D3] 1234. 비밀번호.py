for TC in range(1,11):
    N, string = input().split()
    stack = []
    for i in range(0, int(N)):
        if stack:
            # 중복이면 제거
            if stack[-1] == string[i]:
                stack.pop()
            # 중복이 아니면 추가
            else:
                stack.append(string[i])
        else:
            stack.append(string[i])
    password = ''.join(map(str, stack))
    print(f'#{TC} {password}')