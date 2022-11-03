n = int(input())
words = input()
ans = 0
for idx, word in enumerate(words):
    ans += (ord(word) - 96)*31**idx
    ans %= 1234567891
print(ans)