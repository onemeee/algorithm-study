n = int(input())
wait = list(map(int, input().split()))
wait.sort()
wait_sum = [wait[0]]
for i in range(1, n):
    wait_sum.append(wait_sum[i-1]+wait[i])
print(sum(wait_sum))
