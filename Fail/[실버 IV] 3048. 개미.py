n1, n2 = map(int, input().split())
team1 = list(input())
team2 = list(input())
copyteam1 = team1.copy()
copyteam2 = team2.copy()
t = int(input())
move = t-1
for i in range(t):
    if i - move - 1 < 0:
        team2[abs(i-move)] = copyteam1[i]
        team1[abs(i-move)] = copyteam2[i]
    else:
        team1[i-move - 1] = copyteam1[i]
        team2[i-move - 1] = copyteam2[i]
    move -= 1
road = team1[::-1] + team2
print(''.join(road))
