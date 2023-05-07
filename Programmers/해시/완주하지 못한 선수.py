from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion) 
    return(''.join(list(answer)))