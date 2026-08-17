def solution(n, m):
    answer = []
    min=0
    max=0
    for i in range(1, n+1):
        if n % i == 0 and m % i == 0:
            min = i
    

    for j in range(n,1000000000,1):
        if j%n==0 and j%m==0:
            max=j
            break
    answer=[min,max]
    return answer