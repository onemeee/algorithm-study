def mymax(a,b):
    if a > b:
        return a
    return b

def findleng(arr):
    max_leng = 0
    for row in arr:
        for i in range(100):
            for j in range(100,-1,-1):
                if j-i+1 > max_leng:
                    word = row[i:j]
                    if word == word[::-1]:
                        leng = len(word)
                        max_leng = mymax(max_leng, leng)
                        break
    return max_leng

for _ in range(10):
    TC = int(input())
    grid = [list(input()) for _ in range(100)]
    grid_rev = [[grid[j][i] for j in range(100)] for i in range(100)]
    max_row = findleng(grid)
    max_col = findleng(grid_rev)
    max_val = mymax(max_row, max_col)

    print(f'#{TC} {max_val}')