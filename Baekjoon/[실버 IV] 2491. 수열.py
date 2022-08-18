N = int(input())
num_list = list(map(int, input().split()))
reverse_list = num_list[::-1]
def findlength(num_list):
    length = 0
    tmp = []
    for idx, num in enumerate(num_list):
        if idx == 0 or tmp[-1] <= num:
            tmp.append(num)
            if len(tmp) > length:
                length = len(tmp)
        else:
            tmp.clear()
            tmp.append(num)
    return length
leng = findlength(num_list)
re_leng = findlength(reverse_list)
result = max(leng, re_leng)
print(result) 