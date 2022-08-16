from itertools import combinations 

num_list = []
for i in range(12): # 1~12까지 숫자가 들어있는 리스트 생성
    num_list.append(i+1)

for TC in range(1, int(input())+1):
    count = 0
    num, total = map(int, input().split())
    subsets = list(combinations(num_list, num)) # 위에서 입력받은 num의 개수로 이루어진 부분 집합 전부 구하기
    for subset in subsets:
        if sum(subset) == total: # 부분집합의 합이 원하는 total 합과 같으면
            count += 1 # count 상승
    print(f'#{TC} {count}')    
            
