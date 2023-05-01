import sys
from heapq import heappush, heappop

input = sys.stdin.readline
heap = []
for i in range(int(input())):
    val = int(input())
    if val == 0:
        if len(heap) == 0:
            print(0)
            continue
        print(heappop(heap))
        continue
    heappush(heap, val)