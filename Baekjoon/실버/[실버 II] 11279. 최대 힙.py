import sys
from heapq import heappush, heappop
input = sys.stdin.readline


def solution(n):
    heap = []
    for _ in range(n):
        val = int(input())
        if val == 0:
            if len(heap) == 0:
                print(0)
                continue
            print(-1 * heappop(heap))
            continue
        heappush(heap, -val)

n = int(input())
solution(n)