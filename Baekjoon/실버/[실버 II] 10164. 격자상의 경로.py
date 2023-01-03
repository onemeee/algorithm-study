def fact(n):
    dp = [1] * (n+1)
    for i in range(1, n+1):
        dp[i] = i * dp[i-1]
    return dp[n]

n, m, k = map(int, input().split())
dires = [(1, 0), (0, 1)]
cnt = 0
cnt2 = 0
if not k:
    a = fact(n+m-2)
    b = fact(n-1)
    c = fact(m-1)
    print(a//(b*c))
else:
    tj = k%m
    if k%m:
        ti = k//m
        tj -= 1
    else:
        ti = k//m - 1
        tj = m - 1
    a = fact(ti+tj)
    b = fact(ti)
    c = fact(tj)
    d = fact((n-ti-1)+(m-tj-1))
    e = fact(n-ti-1)
    f = fact(m-tj-1)
    print((a//(b*c)) * (d//(e*f)))