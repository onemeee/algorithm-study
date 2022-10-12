def find(a,b):
    while True:
        k = b % a
        if not k:
            return a
        b = a
        a = k
            
d1, d2 = map(int, input().split())
dic = {}
for r in range(d1, d2+1):
    for i in range(r):
        if i == 0:
            a = 0
            b = 0
        else:
            c = find(i, r)
            a = i//c
            b = r//c
        if not f'{a}/{b}' in dic:
            dic[f'{a}/{b}'] = 1
print(len(dic))