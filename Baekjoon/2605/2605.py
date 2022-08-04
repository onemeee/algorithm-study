N = int(input())
order = list(map(int, input().split()))
place = []
for i in range(N):
    place.insert(i-order[i], i+1)
print(' '.join(map(str, place)))
