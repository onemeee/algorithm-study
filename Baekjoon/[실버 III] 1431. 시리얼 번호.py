import sys
input = sys.stdin.readline

def cal(word):
    sum_val = 0
    for i in word:
        if i.isdigit():
            sum_val += int(i)
    return sum_val

dic = {}
num_list = []
for i in range(int(input())):
    word = input().rstrip()
    num = len(word)
    if num not in num_list:
        num_list.append(num)
    if num in dic:
        dic[num].append(word)
    else:
        dic[num] = [word]

num_list.sort()
for num in num_list:
    tmp = dic.get(num)
    for i in range(len(tmp)-1):
        for j in range(len(tmp)-1-i):
            if cal(tmp[j]) > cal(tmp[j+1]):
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
            elif cal(tmp[j]) == cal(tmp[j+1]):
                for k in range(num):
                    if tmp[j][k] == tmp[j+1][k]:
                        continue
                    else:
                        if ord(tmp[j][k]) > ord(tmp[j+1][k]):
                            tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
                            break
                        break
    for result in tmp:
        print(result)
