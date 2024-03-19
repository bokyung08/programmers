def solution(s):
    answer = []
    if len(s)%2!=0:
        answer.append(list(s)[len(s)//2])
    else:
        answer.append(list(s)[(len(s)//2)-1])
        answer.append(list(s)[len(s)//2])
        
    return ''.join(answer)