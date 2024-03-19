def solution(n):
    answer = 0
    for i in range(0,n+1,1):
        if i**2==n:
            answer=(i+1)**2
            break
        elif i==n:
            answer=-1
        else:
            continue
        
    return answer