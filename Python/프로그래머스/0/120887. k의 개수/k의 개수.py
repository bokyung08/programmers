def solution(i, j, k):
    answer = 0
    for a in range(i, j+1):
        l=str(a)
        for h in range(len(l)):
            if k==int(l[h]):
                answer+=1
            continue
    return answer