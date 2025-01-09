def solution(myString):
    str=""
    myString=list(myString)
    for i in range(0,len(myString),1):
        if myString[i]<'l':
            str+="l"
        else:
            str+=myString[i]
    return str
