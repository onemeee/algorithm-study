# max 값 찾기 함수 정의
def mymax(a, b):
    if a >= b:
        return a
    return b

# min 값 찾기 함수 정의
def mymin(a, b):
    if a <= b:
        return a
    return b

N = int(input()) # 내용의 길이
maze = list(input()) # 적은 내용 

x, y = 0, 0
delta = [[0, 1], [-1, 0], [0, -1], [1, 0]] # 남, 서, 북, 동
direc = 0
max_x, min_x, max_y, min_y = 0, 0, 0, 0

for info in maze:
    direc %= 4 # direc의 값이 3보다 커지는 것을 방지
    if info == 'R':
        direc += 1
    elif info == 'L':
        direc -= 1
    else:
        x += delta[direc][0]
        y += delta[direc][1]
        max_x = mymax(max_x, x)
        max_y = mymax(max_y, y)
        min_x = mymin(min_x, x)
        min_y = mymin(min_y, y)

maze_grid = [['#'] * (max_x-min_x+1) for _ in range(max_y-min_y+1)]
cx, cy = -min_x, -min_y
maze_grid[cy][cx] = '.'
direc = 0
for info in maze:
    direc %= 4 # direc의 값이 3보다 커지는 것을 방지
    if info == 'R':
        direc += 1
    elif info == 'L':
        direc -= 1
    else:
        cx += delta[direc][0]
        cy += delta[direc][1]
        maze_grid[cy][cx] = '.'
# print
for i in maze_grid:
    print(*i, sep='')