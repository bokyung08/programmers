def solution(arr):
    answer = []
    cnt=0
    for i in arr:
        while(cnt!=i):
            answer.append(i)
            cnt+=1
        cnt=0
    return answer