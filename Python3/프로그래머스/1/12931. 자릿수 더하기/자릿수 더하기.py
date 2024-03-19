def solution(n):
    answer =  list(map(int,str(n)))
    sum=0
    for i in answer:
        sum+=int(i)
    
    return sum