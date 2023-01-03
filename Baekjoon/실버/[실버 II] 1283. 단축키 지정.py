import sys
input = sys.stdin.readline

key = []
for _ in range(int(input())):
    flag = False
    words = list(input().split())
    word_list = [list(word) for word in words]
    for i in range(len(word_list)):
        word = word_list[i]
        if word[0].upper() not in key:
            key.append(word[0].upper())
            word_list[i].insert(0, '[')
            word_list[i].insert(2, ']')
            flag = True
        if flag:
            break
    if flag:
        for word in word_list:
            print(''.join(word), end=' ')
        print()
        continue
    else:
        for i in range(len(word_list)):
            word = word_list[i]
            for j in range(1, len(word)):
                if word[j].upper() not in key:
                    key.append(word[j].upper())
                    word_list[i].insert(j, '[')
                    word_list[i].insert(j+2, ']')
                    flag = True
                    break
            if flag:
                break
    for word in word_list:
        print(''.join(word), end=' ')
    print()
