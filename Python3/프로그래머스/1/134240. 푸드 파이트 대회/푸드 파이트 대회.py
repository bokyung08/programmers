def solution(food):
    result=""
    r=""
    for i in range(1,len(food),1):
        a=food[i]//2
        for j in range(a):
            result+=str(i)
    for i in range(len(result)-1,-1,-1):
        r+=result[i]
    result+="0"
    result+=r
    return result