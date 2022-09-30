import sys
input = sys.stdin.readline

n = int(input())
my_cards = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
dict = {}
for i in check:
    dict[i] = 0
for my in my_cards:
    if my in dict:
        dict[my] += 1
for i in check:
    print(dict[i], end = ' ')