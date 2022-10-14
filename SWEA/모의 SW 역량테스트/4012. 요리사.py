def sum_val(num_list):
    val = 0
    k = len(num_list)
    for i in range(k):
        for j in range(i+1, k):
            val += foods[num_list[i]-1][num_list[j]-1]
            val += foods[num_list[j]-1][num_list[i]-1]
    return val

def combi(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in combi(arr[i+1:], r-1):
                yield [arr[i]] + next

for tc in range(1, int(input())+1):
    min_val = float('INF')
    n = int(input())
    foods = [list(map(int, input().split())) for _ in range(n)]
    food = [i for i in range(1, n+1)]
    for order in combi(food, n//2):
        sum1 = sum_val(order)
        order2 = []
        for num in food:
            if num not in order:
                order2.append(num)
        sum2 = sum_val(order2)
        min_val = min(min_val, abs(sum1-sum2))
    print(f'#{tc} {min_val}')