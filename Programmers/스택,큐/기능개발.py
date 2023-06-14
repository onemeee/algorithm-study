from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        remain = progresses.popleft()
        speed = speeds.popleft()
        release = math.ceil((100 - remain)/speed)
        cnt = 1
        
        for i in range(len(progresses)):
            if math.ceil((100 - progresses[i])/speeds[i]) > release:
                for _ in range(cnt-1):
                    progresses.popleft()
                    speeds.popleft()
                break
            else:
                cnt += 1
        else:
            if cnt > 1:
                for _ in range(cnt-1):
                    progresses.popleft()
                    speeds.popleft()
                    
        answer.append(cnt)
            
    return answer