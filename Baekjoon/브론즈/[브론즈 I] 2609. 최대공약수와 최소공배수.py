n, m = map(int, input().split())
rn, rm = n, m
k = max(n, m)

max_val = 1

for i in range(k, 0, -1):
    if (n % i == 0) and (m % i == 0):
        max_val *= i
        n //= i
        m //= i
    if n == 1 or m == 1:
        break

min_val = (max_val) * (rn//max_val) * (rm//max_val)
print(max_val)
print(min_val)