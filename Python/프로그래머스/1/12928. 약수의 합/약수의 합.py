def solution(n):
    answer=1
    if n==1:
        answer=1
    elif n==0:
        answer=0
    for i in range(2,n+1,1):
        if n%i==0:
            answer+=i

    return answer