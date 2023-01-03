import sys
input = sys.stdin.readline

que = [0]
total = 0
result = []
n = int(input())
for _ in range(n):
    num = int(input())
    while True:
        if que[-1] < num:
            total += 1
            if total > n:
                result = ['NO']
                break
            que.append(total)
            result.append('+')
        elif que[-1] > num:
            result.append('-')
            que.pop()
        elif que[-1] == num:
            result.append('-')
            que.pop()
            break
        if total >= n and que == [0]:
            result = ['NO']
            break
for re in result:
    print(re)