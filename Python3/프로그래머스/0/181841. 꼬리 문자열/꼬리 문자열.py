def solution(str_list, ex):
    answer = ''
    for i in range(0,len(str_list),1):
        if ex in str_list[i]:
            continue
        else: 
            answer+=str_list[i]
    return answer