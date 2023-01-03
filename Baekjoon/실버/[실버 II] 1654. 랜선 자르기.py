import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
left = 0
right = max(lines)
tmp_ans = []
while left <= right:
    tmp = 0
    mid = (left+right)//2
    for line in lines:
        if mid:
            tmp += line//mid
        else:
            tmp += line
    if tmp >= n:
        tmp_ans.append(mid)
        left = mid+1
    else:
        right=mid-1
ans = max(tmp_ans)
print(ans)