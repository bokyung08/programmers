def solution(x):
    li=list(str(x))
    s=0
    for i in range(len(li)):
        s+=int(li[i])
    if x%s==0:
        answer = True
    else:
        answer=False

    return answer