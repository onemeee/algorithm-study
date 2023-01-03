import sys
input = sys.stdin.readline

def dfs(idx, val):
    global max_val
    global min_val
    global n
    
    if idx == n:
        max_val = max(max_val, val)
        min_val = min(min_val, val)
    else:
        for i in range(4):
            if opers[i]:
                opers[i] -= 1
                if i == 0:
                    dfs(idx+1, val+num_list[idx])
                elif i == 1: 
                    dfs(idx+1, val-num_list[idx])
                elif i == 2: 
                    dfs(idx+1, val*num_list[idx])
                elif i == 3: 
                    if val < 0:
                        dfs(idx+1, -1*(abs(val)//num_list[idx]))
                    elif val >= 0:
                        dfs(idx+1, val//num_list[idx])
                opers[i] += 1

n = int(input())
num_list = list(map(int, input().split()))
opers = list(map(int, input().split()))
max_val = -1e9
min_val = 1e9
dfs(1, num_list[0])
print(max_val)
print(min_val)