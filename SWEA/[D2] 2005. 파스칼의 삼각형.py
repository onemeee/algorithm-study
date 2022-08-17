def Pascal(n):
    def factorial(m, repeat):
        result = 1
        k = 0
        while k < repeat:
            result *=m
            k += 1
            m -= 1 
        return result
    pascal = []
    for i in range(n+1):
        if i == 0 or i ==n :
            pascal.append(1)
        else:
            numer = factorial(n, i)
            deno = factorial(i, i)
            pascal.append(numer//deno)
    return pascal
            
for TC in range(1, int(input())+1):
    print(f'#{TC}')
    for i in range(int(input())):
        if i == 0:
            print(1)
        else:
            print(' '.join(map(str, Pascal(i))))
