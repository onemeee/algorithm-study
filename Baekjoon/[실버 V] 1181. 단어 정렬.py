import sys
input = sys.stdin.readline

dic = {}
check = []
for _ in range(int(input())):
    word = input().rstrip()
    n = len(word)
    if n in dic:
        if word not in dic[n]:
            dic[n].append(word)
    else:
        dic[n] = [word]
        check.append(n)
check.sort()
for i in check:
    words = dic[i]
    words.sort()
    for word in words:
        print(word)
    