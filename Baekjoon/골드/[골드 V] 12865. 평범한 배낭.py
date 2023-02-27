import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
infos = [tuple(map(int, input().rstrip().split())) for _ in range(n)]

result = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):                 # 물건의 개수 n개
    for j in range(1, k+1):             # 허용 무게 k까지
        if infos[i-1][0] <= j:            # i번째 물건의 무게가 j보다 작거나 같은 경우
            result[i][j] = max(result[i-1][j-infos[i-1][0]] + infos[i-1][1], result[i-1][j])
        else:
            result[i][j] = result[i-1][j]

print(result[n][k])