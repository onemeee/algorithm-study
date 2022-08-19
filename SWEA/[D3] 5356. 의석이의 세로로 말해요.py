for tc in range(1, int(input())+1):
    words = [[''] * 15 for _ in range(5)]
    leng_max = 0
    for i in range(5):
        word = input()
        leng = len(word)
        leng_max = max(leng_max, leng)
        for j in range(leng):
            words[i][j] = word[j]
    result = ''
    for j in range(leng_max):
        for i in range(5):
            result += words[i][j]
    print(f'#{tc} {result}')