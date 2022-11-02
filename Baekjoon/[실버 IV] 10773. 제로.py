import sys
input = sys.stdin.readline

prices = []
n = int(input())
for _ in range(n):
    price = int(input())
    if price:
        prices.append(price)
    else:
        prices.pop()
print(sum(prices))