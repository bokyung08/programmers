def solution(elements): 
    n = len(elements)
    cir= elements*2
    sums= set()
    for i in range(1, n+1): 
        current= sum(cir[:i])
        sums.add(current)
        for j in range(1,n): 
            current -=cir[j-1]
            current += cir[i + j-1]
            sums.add(current)
    return len(sums)