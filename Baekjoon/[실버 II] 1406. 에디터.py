import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []
for _ in range(int(input())):
    cmd = list(input().split())
    if cmd[0] == 'L':
        if not left:
            continue
        right.append(left.pop())
    elif cmd[0] == 'D':
        if not right:
            continue
        left.append(right.pop())
    elif cmd[0] == 'B':
        if not left:
            continue
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])
print(''.join(left+right[::-1]))