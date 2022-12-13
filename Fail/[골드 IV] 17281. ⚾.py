import sys
input = sys.stdin.readline

def play():
    # 이닝에 대한 각 선수 결과
    results = [ list(map(int, input().split())) for _ in range(n)]
    
    # 타순 결정하기
    nums = list(range(1, 10))
    for ord in player(nums, 8):
        orders = ord[:3] + [0] + ord[3:]
        score = 0
        start = 0
        for result in result:
            out = 0
            while out <= 3:
                rst = result[start]
                if rst == 0:
                    pass

# 타순 결정
def player(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for next in player(arr[:i] + arr[i+1], r-1):
                yield [arr[i]] + next    
    
