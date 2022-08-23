import sys
input = sys.stdin.readline

stack = [] # 숫자 담기

n = int(input())
infos = input().rstrip()

# 알파벳 숫자로 만들기 위한 dict
alpha = {}
for i in range(n):
    alpha[chr(65+i)] = int(input())
for info in infos:
    if info.isalpha():
        info = alpha.get(info)
        stack.append(info)
    else:
        val1 = stack.pop()
        val2 = stack.pop()
        if info == '+':
            val = val2 + val1
        elif info == '-':
            val = val2 - val1
        elif info == '*':
            val = val2 * val1
        elif info == '/':
            val = val2 / val1
        stack.append(val)
print(f'{stack.pop():.2f}')
