def findload(list):
    tmp = []
    count = 0
    for word in list:
        if word == 1:
            count += 1
        else:
            tmp.append(count)
            count = 0
    if count != 0:
        tmp.append(count)
    return tmp

def findword(list, target):
    count = 0
    for row in list:
        leng = findload(row)
        for i in leng:
            if i == target: 
                count += 1
    return count

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    count = 0
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    puzzle_rev = [[puzzle[i][j] for i in range(N)] for j in range(N)]
    a = findword(puzzle, K)
    b = findword(puzzle_rev, K)
    print(f'#{tc} {a+b}')