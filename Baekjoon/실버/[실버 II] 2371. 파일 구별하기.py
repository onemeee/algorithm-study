import sys
input = sys.stdin.readline

n = int(input())
given_infos = [list(map(int, input().split()))[:-1] for _ in range(n)]
max_len = 0
for info in given_infos:
    max_len = max(max_len, len(info))
infos = []
for info in given_infos:
    k = len(info)
    info = info+ [0] * (max_len - k)
    infos.append(info)
length = 0
while length < max_len:
    tmp = 0
    check = []
    length += 1
    for info in infos:
        tmp_info = info[0:length]
        if tmp_info in check:
            break
        check.append(tmp_info)
        tmp += 1
    if tmp == n:
        break
print(length)
