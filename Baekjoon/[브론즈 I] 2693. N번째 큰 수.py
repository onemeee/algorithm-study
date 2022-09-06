import sys
input = sys.stdin.readline
for _ in range(int(input())):
    num_list = sorted(list(map(int, input().split())), reverse=True)
    print(num_list[2])
