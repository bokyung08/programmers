def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1,1):
        lim=0
        for j in range(1,int(i**(1/2)+1)):
            if i%j==0: 
                lim +=1
                if j<i//j:
                    lim+=1
        if lim>limit:
            answer+=power
        else:
            answer+=lim
    return answer