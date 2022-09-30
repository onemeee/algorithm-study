n, k = map(int, input().split())
val = 1
val2 = 1
for _ in range(k):
    val *= n
    val2 *= k
    n -= 1
    k -= 1
print(val//val2)