def solution(targets):
    check = -1
    targets.sort(key= lambda x:x[1])
    
    answer=0
    for idx in range(len(targets)):
        if check <= targets[idx][0]:
            check= targets[idx][1]
            answer+=1
    return answer