n = int(input())
foods = list(map(int, input().split()))
results = [0] * n
results[0] = foods[0]
results[1] = max(results[0], foods[1])
for i in range(2, n):
    results[i] = max(results[i-1], results[i-2]+foods[i])
print(results[-1])