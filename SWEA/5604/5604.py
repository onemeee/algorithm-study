for i in range(int(input())):
    A, B = map(int, input().split())
    sum = 0
    for num in range(A, B+1):
        for k in str(num):
            sum += int(k)
    print(f'#{i+1} {sum}')