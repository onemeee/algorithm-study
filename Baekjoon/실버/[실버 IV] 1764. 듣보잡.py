import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nolisten = set(input().rstrip() for _ in range(n))
nosee = set(input().rstrip() for _ in range(m))
nolisee = list(nolisten & nosee)
nolisee.sort()
print(len(nolisee))
for name in nolisee:
    print(name)
     