import sys
input = sys.stdin.readline

def findcases():
    global _
    n = input().rstrip()
    if not n:
        print(0)
        return
    calc = [0] * len(n)
    flag = False
    for i in range(len(n)):
        if i == 0:
            if n[i] == '0':
                print(0)
                return
            else:
                calc[i] = 1
        elif i == 1:
            if i+1 <= len(n)-1:
                if n[i+1] == '0':
                    calc[i] = calc[i-1]
                    continue
            if int(n[0:2])<= 26 and n[i] != '0':
                calc[i] = calc[i-1] + 1
                flag = True
            elif n[i] == '0' and int(n[0:2]) > 26:
                print(0)
                return
            else:
                calc[i] = calc[i-1]
        else:
            if int(n[i-1:i+1]) <= 26 and n[i] != '0' and n[i-1] != '0':
                if i+1 <= len(n)-1:
                    if n[i+1] == '0':
                        calc[i] = calc[i-1]
                        continue
                if flag:
                    calc[i] = calc[i-1] + calc[i-2]
                else:
                    calc[i] = calc[i-1] * 2
                    flag = True
            elif n[i] == '0' and n[i-1] == '0':
                print(0)
                return
            elif n[i] == '0' and int(n[i-1:i+1]) > 26:
                print(0)
                return
            else:
                calc[i] = calc[i-1]
                flag = False
    print(calc[-1]%1000000)
findcases()
