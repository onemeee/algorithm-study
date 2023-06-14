import sys
input = sys.stdin.readline

n = int(input())
infos = [list(map(int, input().rstrip().split())) for _ in range(n)]
persons = [i  for i in range(n)]
ans = 1e9

def partition(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]]
        else:
            for next in partition(arr[i+1:], k-1):
                yield [arr[i]] + next

# start 팀 정보
for start in partition(persons, n//2):
    link = [ i for i in range(n) if i not in start ]
    
    s_score = 0
    l_score = 0

    for i in range(n//2-1):
        for j in range(i+1, n//2):
            s_score += (infos[start[i]][start[j]] + infos[start[j]][start[i]])
            l_score += (infos[link[i]][link[j]] + infos[link[j]][link[i]])

    value = abs(s_score-l_score)
    ans = min(ans, value)

print(ans)