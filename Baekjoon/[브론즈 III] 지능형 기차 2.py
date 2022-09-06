import sys
input = sys.stdin.readline

infos = [ list(map(int, input().split())) for _ in range(10) ]
max_num = 0
num =0

for info in infos:
    num -= info[0]
    num += info[1]
    max_num = max(max_num, num)

print(max_num)