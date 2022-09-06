import sys
input = sys.stdin.readline

stack = []
infos = input()
tmp = 1
result = 0

for i in range(len(infos)):
    if infos[i] == '(':
        stack.append(infos[i])
        tmp *= 2
    elif infos[i] == '[':
        stack.append(infos[i])
        tmp *= 3
    elif infos[i] == ')':
        if stack and stack[-1] == '(':
            stack.pop()
            if infos[i-1] == '(':
                result += tmp
            tmp //= 2
        else:
            result = 0
            break
    elif infos[i] == ']':
        if stack and stack[-1] == '[':
            if infos[i-1] == '[':
                result += tmp
            stack.pop()
            tmp //= 3
        else:
            result = 0
            break
if stack:
    print(0)
else:
    print(result)
