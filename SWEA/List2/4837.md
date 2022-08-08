실수로 문제를 잘못 읽어, 1~12개의 수 중 3개를 합쳐 원하는 수를 만드는 case의 개수를 세는 것으로 착각  
만든 코드가 아까워 .. 남겨두기!
```python
for TC in range(1, int(input())+1):
    num, total = map(int, input().split())
    count = 0
    for i in range(1, 11):
        start = i
        left = i + 1
        right = 12
        while True:
            sum_num = start + left + right
            if left >= right:
                break
            else:
                if sum_num == total:
                    count += 1
                    print(start, left, right)
                    break
                elif sum_num < total:
                    left += 1
                elif sum_num > total:
                    right -= 1
    print(f'#{TC} {count}')     
```