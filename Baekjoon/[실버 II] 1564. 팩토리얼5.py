import sys
input = sys.stdin.readline

N = int(input())
val = 1
for i in range(2, N+1):
    val *= i
    while val %10 ==  0:
        val //= 10
    val %=100000000000000000
val %= 100000
print('%05d' %val)