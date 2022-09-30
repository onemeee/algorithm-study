import sys
input = sys.stdin.readline

while True:
    leng = sorted(list(map(int, input().split())))
    a, b, c = leng[0], leng[1], leng[2]
    if a == 0:
        break
    if c**2 == b**2 + a** 2:
        print('right')
    else:
        print('wrong')