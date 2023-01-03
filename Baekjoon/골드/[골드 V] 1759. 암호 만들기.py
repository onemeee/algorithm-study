import sys
input = sys.stdin.readline

def combi(arr, n):
    for i in range(len(arr)):
        if n == 1:
            yield [arr[i]]
        else:
            for next in combi(arr[i+1:], n-1):
                yield [arr[i]] + next

n, m = map(int, input().split())
words = sorted(list(input().split()))

for word in combi(words, n):
    flag = False
    num = 0
    for vow in ['a', 'e', 'i', 'o', 'u']:
        num += word.count(vow)
        if num > n-2:
            flag = True
            break
    if flag:
        continue
    if num:
        print(''.join(word))
