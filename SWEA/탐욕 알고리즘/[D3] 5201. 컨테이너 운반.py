for tc in range(1, int(input())+1):
    n, m = map(int, input().split()) # 컨테이너 수, 트럭 수
    weights = sorted(list(map(int, input().split())), reverse=True) # 화물 무게
    limits = sorted(list(map(int, input().split())), reverse=True) # 적재 용량
    result = 0
    idx = 0
    for i in range(m):
        if idx < n:
            while weights[idx] > limits[i]:
                idx += 1
                if idx >= n:
                    break
            if idx < n:
                result += weights[idx]
                idx += 1
        else:
            break
    print(f'#{tc} {result}')