def solution(my_string, is_suffix):
    answer = []
    if is_suffix in my_string:
        if is_suffix[-1]==my_string[-1]:
            return 1
        else:
            return 0
    return 0