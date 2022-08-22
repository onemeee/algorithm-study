import sys
input = sys.stdin.readline

stack1 = [] # 숫자 담기
stack2 = [] # 연산 담기

n = int(input())
infos = input()

alpha = {}
for i in range(n):
    alpha[chr(65+i)] = int(input())

flag = False
cnt = 0

for info in infos:
    if flag == True:
        if info.isalpha():
            val = stack1.pop()
            while stack2:
                cal = stack2.pop()
                if cal == '*':
                    val *= stack1.pop()
                elif cal == '/':
                    val /= stack1.pop()
                elif cal == '+':
                    val += stack1.pop()
                elif cal == '-':
                    val -= stack1.pop()
                print(val)
            info = alpha.get(info)
            stack1.append(info)
            flag = False
        else:
            stack2.append(info)
    else:
        if info.isalpha():
            info = alpha.get(info)
            cnt += 1
            stack1.append(info)
        else:
            stack2.append(info)
            flag = True
print(val)
