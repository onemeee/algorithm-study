import sys
input = sys.stdin.readline

def find(oper_list, new=[]):
    global new_opers
    if not len(oper_list):
        if new in new_opers:
            pass
        else:
            new_opers.append(new)
    for i in range(len(oper_list)):
        new_oper = new + [oper_list[i]]
        new_list = oper_list[0:i] + oper_list[i+1:]
        find(new_list, new_oper)

n = int(input())
num_list = list(map(int, input().split()))
num_list.reverse()
opers = list(map(int, input().split()))
oper_list = []
new_opers = []

for i in range(len(opers)):
    while opers[i] != 0:
        if i == 0:
            oper_list.append('+')
        elif i == 1:
            oper_list.append('-')
        elif i == 2:
            oper_list.append('*')
        elif i == 3:
            oper_list.append('//')
        opers[i] -= 1

find(oper_list)

max_val = -1000000000
min_val = 1000000000

for oper in new_opers:
    cal_list = num_list.copy()
    for i in range(n-1):
        a = cal_list.pop()
        b = cal_list.pop()
        if oper[i] == '//':
            a = abs(a)
        cal_list.append(eval(f'{a}{oper[i]}{b}'))

    cal = cal_list[-1]
    if cal > max_val:
        max_val = cal
    if min_val > cal:
        min_val = cal

print(max_val)
print(min_val)
