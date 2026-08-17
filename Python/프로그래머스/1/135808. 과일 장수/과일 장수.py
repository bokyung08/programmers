def solution(k, m, score):
    score=sorted(score, reverse=True)
    money=0
    n=m
    while True:
        if len(score)<n:
            break
        money+=score[n-1]*m
        n+=m
        
    return money