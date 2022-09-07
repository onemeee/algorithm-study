def back(idx, sum_val):
    global result

    if idx >= n:
        return
    
    tmp_val = sum_val + num_list[idx]

    if tmp_val == s:
        result += 1
    
    # 더해서 다음 단계
    back(idx+1, tmp_val)
    # 더하지 않고 다음단계
    back(idx+1, sum_val)    

n, s = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
result = 0
back(0, 0)
print(result)