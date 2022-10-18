import sys 
input = sys.stdin.readline

def find(s, l):
    while s <= l:
        mid = (s + l) // 2
        tmp = 0
        for tree in trees:
            if tree > mid:
                tmp += tree - mid
        if tmp >= m:
            check.append(mid)
            s = mid + 1
        else:
            l = mid - 1

n, m = map(int, input().split())
trees = list(map(int, input().split()))
s = 0
l = max(trees)
check = []
find(s, l)

print(max(check))