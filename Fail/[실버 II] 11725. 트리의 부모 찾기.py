import sys
input = sys.stdin.readline

n = int(input())
left = [0] * (n+1)
right = [0] * (n+1)
for _ in range(n):
    a, b = map(int, input().split())
    