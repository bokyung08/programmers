def solution(n):
    answer =list(map(int,str(n)))
    answer.sort(reverse=True)
    a=''.join(map(str,answer))
    return int(a)