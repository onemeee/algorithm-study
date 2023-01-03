a, b, v = map(int, input().split())

k = a - b
day = 1
if (v-a)%k:
    day += (v-a)//k
    day += 1
else:
    day += (v-a)//k
print(day)