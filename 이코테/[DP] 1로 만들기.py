n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    if not i % 5:
        dp[i] = min(dp[i//5]+1, dp[i-1]+1)
    elif not i % 3:
        dp[i] = min(dp[i//3]+1, dp[i-1]+1)
    elif not i % 2:
        dp[i] = min(dp[i//2]+1, dp[i-1]+1)
    else:
        dp[i] = dp[i-1] + 1
print(dp[n])