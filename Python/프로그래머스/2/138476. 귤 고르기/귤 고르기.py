from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    t = Counter(tangerine)
    # 개수 기준 내림차순 정렬
    counts = sorted(t.values(), reverse=True) # Values 만 들어감 
    #print(counts)
    for c in counts:
        k -= c
        answer += 1
        
        if k <= 0:
            break
    
    return answer