def solution(s):
    li=[]
    for i in s:
        if i =='(':
            li.append(i)
        else:
            if len(li)==0:
                return False
            else:
                li.pop()
    if len(li)==0:
        return True
    else:
        return False
    