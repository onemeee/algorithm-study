def Permutation(arr, n): # 중복순열 구현
    for i in range(len(arr)):
        if n == 1: # 원하는 r이 1이면
            yield [arr[i]] # 하나만 뽑으면 됨
        else:
          # 하나 뽑고 나머지 r-1개에 대해서는 다시 permutation 돌리기
            for next in Permutation(arr, n-1):
                yield [arr[i]] + next
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
for permu in Permutation(num_list, M):
    print(*permu)