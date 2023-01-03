import sys
input = sys.stdin.readline

remain = []
for _ in range(10):
    num = int(input())%42
    if num not in remain:
        remain.append(num)
print(len(remain))