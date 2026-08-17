import math 
from collections import deque
def solution(progresses, speeds): 
    days=[]
    answer=[]
    for i in range(len(progresses)):
        progress=progresses[i]
        speed=speeds[i]
        remain= 100-progress
        day=math.ceil(remain/speed)
        days.append(day)
    days=deque(days)
    while days:
        d=days.popleft()# 일단 하나 꺼내기 
        n=1 #그 날에 배포된 개수 =1
        while days and days[0]<=d: 
            days.popleft()
            n+=1
        answer.append(n)
    return answer