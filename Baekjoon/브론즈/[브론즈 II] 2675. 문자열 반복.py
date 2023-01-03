import sys
input = sys.stdin.readline

for _ in range(int(input())):
    result = ''
    n, s = input().split()
    for word in s:
        for _ in range(int(n)):
            result += word
    print(result)