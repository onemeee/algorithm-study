def findnum(N, num_list):
    n = N
    while True:
        num_list[n%10] += loc
        n = n//10
        if n == 0:
            break

for i in range(int(input())):
    A, B = map(int, input().split())
    sum_num = [0] * 10
    loc = 1

    while A <= B:
        while A % 10 != 0 and A <= B:
            findnum(A, sum_num)
            A += 1
        
        if A > B:
            break

        while B % 10 != 9 and A <= B:
            findnum(B, sum_num)
            if A == B:
                break
            B -= 1

        if A==B:
            break
        
        for k in range(10):
            sum_num[k] += (B//10-A//10+1) * loc

        A = A//10
        B = B//10

        if A == 0 and B == 0:
            break
        loc *= 10

    result = 0
    for j in range(10):
        result += j * sum_num[j]
    print(f'#{i+1} {result}')