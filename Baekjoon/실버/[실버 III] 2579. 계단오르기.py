import sys
input = sys.stdin.readline

def goup():
    n = int(input())
    floors = [int(input()) for _ in range(n)]
    result = [0] * (n+1)

    if n == 1:
        print(floors[0])
        return
    
    elif n ==2:
        print(floors[0] + floors[1])
        return
    
    result[1] = floors[0]
    result[2] = floors[0] + floors[1]

    for i in range(3, n+1):
        result[i] = max(floors[i-1]+result[i-2], result[i-3]+floors[i-2]+floors[i-1])
    print(result[-1])

goup()