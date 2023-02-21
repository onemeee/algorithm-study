n = int(input())
ways = [0] * (n+1)
ways[1] = 1
ways[2] = 3

for i in range(3, n+1):
    ways[i] = (ways[i-1] + 2* ways[i-2]) % 796796
print(ways[-1])