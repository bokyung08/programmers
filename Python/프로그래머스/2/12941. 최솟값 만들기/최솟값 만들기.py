def solution(A,B):
    answer = 0
    A=sorted(A)
    B=sorted(B, reverse=True)
    print(B)
    li=[]
    for i in range(len(A)):
        answer+=A[i]*B[i]
    return answer