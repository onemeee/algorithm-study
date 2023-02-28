import sys
input = sys.stdin.readline

def check():
    n, m = map(int, input().split())
    prefixs = dict()
    ans = 0

    for _ in range(n):
        word = input().rstrip()
        for i in range(1, len(word)+1):
            prefixs[word[:i]] = True

    for _ in range(m):
        prefix = input().rstrip()
        if prefixs.get(prefix) == True:
            ans += 1

    print(ans)

check()