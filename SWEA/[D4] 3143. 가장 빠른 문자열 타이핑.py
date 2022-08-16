def kmpsearch(string, pat): # 문자열에 있는 특정 단어 찾기
    N = len(string) # 문자열의 길이
    M = len(pat) # 패턴의 길이
    lps = [0] * M
    
    computeLPS(pat, lps)

    i = 0 # string idx
    j = 0 # pat idx
    count = 0

    while i < N:
        if pat[j] == string[i]:
            i += 1
            j += 1
        elif pat[j] != string[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        if j == M:
            count += 1
            j = 0
    return count

def computeLPS(pat, lps):
    leng = 0
    i = 1 # lps의 idx, lps[0]은 항상 0이므로 i = 1부터 탐색
    while i < len(pat):
        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1

for TC in range(1, int(input())+1):
    A, B = input().split()
    cnt = kmpsearch(A, B)
    min_cnt = len(A) - (len(B)-1)*cnt # B의 개수
    print(f'#{TC} {min_cnt}')