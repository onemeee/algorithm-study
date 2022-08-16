for TC in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    result = 0
    for str in str1:
        tmp_count = str2.count(str)
        if tmp_count > result:
            result = tmp_count
    print(f'#{TC} {result}')