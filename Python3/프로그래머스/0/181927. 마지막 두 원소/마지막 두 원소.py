def solution(num_list):
    answer = []
    if num_list[-1]>num_list[-2]:
        num_list.append(num_list[-1]-num_list[-2])
    else:
        num_list.append(2*num_list[-1])
    return num_list