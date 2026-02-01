
def solution(a, b, n):
    answer=0
    while n>=a:
        ch=(n//a)*b
        re=n%a
        answer+=ch
        n=ch+re
    return answer