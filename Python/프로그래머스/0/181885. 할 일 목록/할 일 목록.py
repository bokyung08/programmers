def solution(todo_list, finished):
    answer = []
    for i in range(0,len(todo_list),1):
        if finished[i]==False:
            answer.append(todo_list[i])
        else: 
            continue
    return answer