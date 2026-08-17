def solution(strArr):
    answer = [0]*len(strArr)
    for i in strArr:
        answer[len(i)]+=1
    return max(answer)