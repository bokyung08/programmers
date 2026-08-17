def solution(s, skip, index):
    alpha="abcdefghijklmnopqrstuvwxyz"
    answer=""
    real_alpha= [x for x in alpha if x not in skip]*5
    print(real_alpha)
    for i in s: 
        where_i=real_alpha.index(i)+index
        answer+= real_alpha[where_i]
    return answer