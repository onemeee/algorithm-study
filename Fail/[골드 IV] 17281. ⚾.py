import sys
input = sys.stdin.readline


# 4번 타자 제외하고 타순 정하기
def player(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in player(arr[:i] + arr[i+1:], r-1):
                yield [arr[i]] + next

def play(players, results):
    global n
    score = 0
    out = 0
    inning = 0
    idx = 0
    locs = [0] * 3

    while inning < n:
        # 한바퀴를 다 돈 경우
        if idx == 9:
            inning += 1
            idx = 0
            continue

        # 아웃인 경우
        if results[inning][players[idx]] == 0:
            out += 1
            if out >= 3:
                inning += 1
                out = 0
                continue
        # 안타이상
        else:
            num = results[inning][players[idx]] - 1
            for i in range(3):
                if locs[i]:
                    locs[i] = 0
                    if i + num >= 3:
                        score += 1
                    else:
                        locs[i+num] = 1
        idx +=1
    return score



n = int(input())
max_score = 0

results = [list(map(int, input().rstrip().split())) for _ in range(n)]
for next in player([0,1,2,4,5,6,7,8], 8):
    tmp_score = play([3] + next, results)
    max_score = max(max_score, tmp_score)
print(max_score)



