import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    info = list(input().split())
    if info[0] == 'add':
        s.add(info[1])
    elif info[0] == 'remove':
        if info[1] in s:
            s.remove(info[1])
    elif info[0] == 'check':
        if info[1] in s:
            print(1)
        else:
            print(0)
    elif info[0] == 'toggle':
        if info[1] in s:
            s.remove(info[1])
        else:
            s.add(info[1])
    elif info[0] == 'all':
        s.clear()
        s.update(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
    elif info[0] == 'empty':
        s.clear()