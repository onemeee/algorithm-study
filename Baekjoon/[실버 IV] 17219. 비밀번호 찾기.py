import sys
input = sys.stdin.readline

n, m = map(int, input().split())
password = dict()
for _ in range(n):
    site, word = input().rstrip().split()
    password[site] = word
for _ in range(m):
    any = input().rstrip()
    print(password[any])
