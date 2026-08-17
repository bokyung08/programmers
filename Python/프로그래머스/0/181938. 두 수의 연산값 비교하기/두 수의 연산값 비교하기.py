def solution(a, b):
    answer = str(a)+str(b)
    if 2*a*b>int(answer):
        return 2*a*b
    else:
        return int(answer) 