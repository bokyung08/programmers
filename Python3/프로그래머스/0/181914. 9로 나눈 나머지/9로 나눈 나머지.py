def solution(number):
    sum=0
    for i in str(number):
        sum+=int(i)
    return sum%9