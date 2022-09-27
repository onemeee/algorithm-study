def cal(company, cost):
    global ans
    if cost >= ans:
        return
    if company == n:
        ans = cost
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        cal(company+1, cost+arr[company][i])
        visited[i] = 0

for tc in range(1, int(input())+1):
    n = int(input())
    ans = 99 * 15
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    print(visited)
    cal(0, 0)
    print(f'#{tc} {ans}')