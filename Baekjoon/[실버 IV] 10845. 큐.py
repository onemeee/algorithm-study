import sys
input = sys.stdin.readline

q = []
for i in range(int(input())):
    cmd = list(input().split())
    if cmd[0] == 'push':
        num = int(cmd[1])
        q.append(num)
    elif cmd[0] == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    