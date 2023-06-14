def solution(nums):
    n = len(nums)
    phonemon = {}
    answer = 0
    for num in nums:
        if phonemon.get(num) == None:
            phonemon[num] = True
            answer += 1
            if answer >= n//2:
                break        
    return answer