### 4831
```python
T = int(input())

for i in range(1,T+1):       #케이스넘버 출력이 편하게 1부터 범위 설정
    N = int(input())         
    cards = list(map(int,input()))     #map을 이용해 스트링으로 받은 문자열숫자를 각각 따로 int형으로 변환해서 리스트로 저장
    counts = 0     #카드의 수를 담는 변수
    whatnum = 0    #카드에 적힌 숫자를 담는 변수 
    for num in cards :       #cards의 요소를 불러옴
        if counts <= cards.count(num) :    #cards에서 해당 요소의 수를 세고, 미리 선언한 counts보다 크거나 같으면
            counts = cards.count(num)      #counts 변수에 요소의 수를 센 것을 저장한다.
            whatnum = max(num,whatnum)     #혹시라도 카운트가 같을 수 있으니 whatnum과 새로운 num 중에 큰 것을 whatnum에 저장
    print(f'#{i} {whatnum} {counts}')      #f 스트링을 이용한 출력
```
동준님 풀이인데, 이게 내가 푼 것보다 훨씬 간단하고 직관적인 것 같다!
