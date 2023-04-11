import sys
input = sys.stdin.readline

n = int(input())

ans = 0
infos = [tuple(map(int, input().rstrip().split())) for _ in range(n)]
infos.sort(key= lambda x : (x[1], x[0]))
before = 0
for start, end in infos:
    if start >= before:
        before = end
        ans += 1
print(ans) 