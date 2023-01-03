import sys
input = sys.stdin.readline

def findsieve(n):
    sieve = []
    for i in range(2, n-1):
        for j in range(2, int(i**0.5)+1):
            if not i%j:
                break
        else:
            sieve.append(i)
    return sieve

for _ in range(int(input())):
    n = int(input())
    sieve = findsieve(n)
    i = 0
    idx = 0
    idx2 = 0
    length = 10000
    while True:
        val = sieve[i]
        val2 = n-val
        if val > val2:
            break
        elif val == val2:
            idx = i
            idx2 = i
            break
        if val2 in sieve:
            tmp_idx = sieve.index(val2)
            if tmp_idx-idx < length:
                length = tmp_idx-i
                idx = i
                idx2 = tmp_idx
            i += 1
        else:
            i +=1
    print(sieve[idx], sieve[idx2])
            
