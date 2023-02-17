arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    # 원소가 1개인 경우
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 left 값 증가
        while left <= right and arr[left] <= arr[pivot]:
            left += 1 
        # 피벗보다 작은 데이터를 찾을 때까지 right 값 감소
        while left <= right and arr[right] >= arr[pivot]:
            right -= 1
        
        # 찾다가 엊갈린 경우,
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각가 정렬 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right + 1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)