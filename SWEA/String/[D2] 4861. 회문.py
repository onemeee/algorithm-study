for TC in range(1, int(input())+1):
    N, M = map(int, input().split())
    str_list = [] # 세로 줄 체크를 위한 list
    for i in range(N):
        string = input()
        for j in range(N-M+1): # 가로 줄에서 회문 체크
            check = string[j:j+M] # 원하는 M만큼의 길이 추출
            if check == check[::-1]: # 회문인지 체크
                result = check
                break
        str_list.append(string)
    for i in range(N): # 세로줄 찾기 시작
        string2 = '' # 세로줄 값을 넣을 문자열 생성
        for j in range(N): 
            string2 += str_list[j][i] # 세로줄 문자열 만들기
        for k in range(N-M+1):
            check2 = string2[k:k+M] # 원하는 M만큼의 길이 추출
            if check2 == check2[::-1]: # 회문인지 체크
                result = check2
                break
    print(f'#{TC} {result}')