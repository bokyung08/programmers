def solution(my_string, indices):
    answer = ''
    my_string=list(my_string)
    for i in range(len(my_string)):
        if i in indices:
            continue
        else:
            answer+=my_string[i]

    return answer