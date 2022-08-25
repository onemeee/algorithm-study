words = list(input())
set_words = set(words)
count = {}
for word in set_words:
    count[word.upper()] = 0
for word in words:
    count[word.upper()] += 1
max_val = 0
for idx, val in count.items():
    if val > max_val:
        max_val = val
        result = idx
    elif max_val == val:
        result = '?'
print(result)