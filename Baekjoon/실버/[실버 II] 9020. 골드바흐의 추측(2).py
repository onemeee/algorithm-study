import sys
input = sys.stdin.readline

def sieve(n):
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    else:
        return True

for _ in range(int(input())):
    n = int(input())
    val = n//2
    val2 = val
    while True:
        if sieve(val) and sieve(val2):
            print(val, val2)
            break
        else:
            val -= 1
            val2 += 1