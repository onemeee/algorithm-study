import sys

stack = []
for _ in range(int(sys.stdin.readline())):
    info = list(sys.stdin.readline().split())
    cmd = info[0]

    if cmd == 'push':
        stack.append(info[1])

    elif cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif cmd == 'size':
        print(len(stack))

    elif cmd == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)