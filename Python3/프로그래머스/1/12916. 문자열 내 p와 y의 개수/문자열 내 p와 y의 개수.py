def solution(s):
    p=0
    y=0
    for i in list(s):
        if i=='p' or i=="P":
            p+=1
        elif i=='y' or i=="Y":
            y+=1
        else:
            continue
    if p==y:
        answer=True
    elif p==0 and y==0:
        answer=True
    else:
        answer=False
    

    return answer