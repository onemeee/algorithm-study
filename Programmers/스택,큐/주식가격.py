from collections import deque

def solution(prices):
    ans = []
    prices = deque(prices)
    while prices:
        now = prices.popleft()
        sec = 0
        
        for price in prices:
            sec += 1
            if now > price:
                break
        ans.append(sec)
    return ans