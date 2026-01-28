def solution(name, yearning, photo):
    answer = []
    score = dict(zip(name, yearning))  # 키-값 매핑
    
    for i in range(len(photo)):
        a=0
        for j in photo[i]:
            if j in name:
                a+=score.get(j)
        answer.append(a)
    return answer