def main():
    a, b = map(int, input().split())
    cnt = 0
    n = 0
    num = 4
    
    if b < num:
        print(cnt)
        return
    
    def quotient(num, k):
        val = (num // 10**k) % 10
        return val
    
    while num <= b:
        if n == 0:
            if quotient(num, 0) == 4:
                if a <= num:
                    cnt += 1
                num += 3
            elif quotient(num, 0) == 7:
                if a <= num:
                    cnt += 1
                num -= 3
                k = 1
                while True:
                    if quotient(num, k) == 4:
                        num += 3 * (10 ** k)
                        break
                    elif quotient(num, k) == 7:
                        num -= 3 * (10 ** k)
                        k += 1
                    elif quotient(num, k) == 0:
                        num += 4 * (10 ** k)
                        break
    print(cnt)
main()

a, b = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    for num in str(i):
        if num != '4' and num != '7':
            break
    else:
        cnt += 1
print(cnt)