alphas = ['q','u','a','c','k']

word = input()
idx = 0
total = 0
flag = False

for wo in word:
    if wo == alphas[idx]:
        idx += 1
    else:
        flag = False
    if idx == 5:
        idx = 0
        if not flag:
           total += 1
        flag = True

if total:
    print(total)
else:
    print(-1)