def findmax(arr, k, l):
    max_arr = sum(arr[0:k])
    last_arr = max_arr
    for i in range(k, l):
        last_arr = last_arr + arr[i] - arr[i-k]
        if max_arr < last_arr:
            max_arr = last_arr
        # max_arr = max(max_arr, last_arr)로 하면 코드가 깔끔할 듯!
        
    return max_arr

N, K = map(int, input().split()) # N 개의 숫자, K개
degrees = list(map(int, input().split()))
print(findmax(degrees, K, N))

