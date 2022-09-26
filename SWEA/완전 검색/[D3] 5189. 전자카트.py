def visit(idx, val, sum_val):
    if val == n-1:
        sum_vals.append(sum_val + grid[idx][0])
        return
    for i in range(1, n):
        if idx != i:
            if not visited[i]:
                visited[i] = 1
                visit(i, val+1, sum_val + grid[idx][i])
                visited[i] = 0
        
for tc in range(1, int(input())+1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n)
    sum_vals = []
    visit(0, 0, 0)
    print(f'#{tc} {min(sum_vals)}')