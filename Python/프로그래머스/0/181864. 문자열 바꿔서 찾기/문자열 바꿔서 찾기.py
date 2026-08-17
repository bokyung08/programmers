def solution(myString, pat):
    myString=list(myString)
    str=""
    for i in range(0,len(myString),1):
        if myString[i]=="A":
            myString[i]="B"
        elif myString[i]=="B":
            myString[i]="A"
        else:
            continue
    for i in range(0,len(myString),1):
        str+=myString[i]
    if pat in str:
        return 1
    else:
        return 0