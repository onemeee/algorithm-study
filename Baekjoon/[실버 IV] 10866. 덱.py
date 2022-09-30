import sys
from collections import deque
input = sys.stdin.readline

deck = deque()
for _ in range(int(input())):
    word = list(input().split())
    if word[0] == 'push_front':
        deck.appendleft(word[1])
    elif word[0] == 'push_back':
        deck.append(word[1])
    elif word[0] == 'pop_front':
        if not len(deck):
            print(-1)
            continue
        print(deck.popleft())
    elif word[0] == 'pop_back':
        if not len(deck):
            print(-1)
            continue
        print(deck.pop())
    elif word[0] == 'size':
        print(len(deck))
    elif word[0] == 'empty':
        if not len(deck):
            print(1)
            continue
        print(0)
    elif word[0] == 'front':
        if not len(deck):
            print(-1)
            continue
        print(deck[0])
    elif word[0] == 'back':
        if not len(deck):
            print(-1)
            continue
        print(deck[-1])