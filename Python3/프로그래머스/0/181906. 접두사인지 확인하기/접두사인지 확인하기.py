def solution(my_string, is_prefix):
    if is_prefix in my_string and my_string[0:len(is_prefix)]==is_prefix[0:len(is_prefix)]:         return 1
    return 0
