n = int(input())
persons = list(range(1, n+1))
idx = 0

for i in range(1, n):
    cnt = i ** 3
    length = len(persons)
    tmp_idx = cnt % length
    idx += tmp_idx - 1
    if idx < 0:
        idx += length
    elif idx >= length:
        idx -= length
    persons.pop(idx)
print(persons[0])
