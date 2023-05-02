import sys
input = sys.stdin.readline

def solution(n):
    work = {}
    names = []
    for _ in range(n):
        name, info = input().rstrip().split()
        if info == 'enter':
            # 출근 - 퇴근 -출근 하는 경우 존재
            if name not in work:
                names.append(name)
            work[name] = 1
        else:
            work[name] = 0
        
    names.sort(reverse=True)
    for name in names:
        if work[name] == 1:
            print(name)
    
n = int(input())
solution(n)