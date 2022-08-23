for TC in range(1, int(input())+1):
    stack = [0] # out of index를 위한 padding
    for word in input(): # 입력받은 문자열을 하나씩 보기
        if stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
        result = len(stack) - 1 # 0에 대한 길이 빼주기
    print(f'#{TC} {result}')