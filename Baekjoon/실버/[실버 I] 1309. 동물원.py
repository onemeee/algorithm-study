n = int(input())

def find(n):
    dp = [0] * (n+1)
    if n == 1:
        print(3)
        return
    dp[1] = 3
    dp[2] = 7
    for i in range(3, n+1):
        dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901

    print(dp[n])

find(n)