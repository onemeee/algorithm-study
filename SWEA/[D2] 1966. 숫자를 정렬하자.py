def counting(list):
    count = [0] * (max(list) + 1)
    for num in list:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    result = [0] * N

    for num in list:
        idx = count[num]
        result[idx-1] = num
        count[num] -= 1
    return result

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted = counting(arr)
    result = ' '.join(map(str, sorted))
    print(f'#{tc} {result}')