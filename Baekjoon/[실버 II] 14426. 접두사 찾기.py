import sys
input = sys.stdin.readline

def check(str):
    k = len(str)
    for word in words:
        if word[:k] == str:
            return True
    return False

n, m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]
ans = 0
for _ in range(m):
    prefix = input().rstrip()
    if check(prefix):
        ans += 1
print(ans)