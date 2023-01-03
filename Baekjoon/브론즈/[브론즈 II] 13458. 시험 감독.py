import sys
input = sys.stdin.readline

n = int(input())
stds = list(map(int, input().split()))
b, c = map(int, input().split())
total = 0
for std in stds:
    total += 1
    std -= b
    if std <= 0:
        continue
    total += std // c
    if std % c:
        total += 1
print(total)
