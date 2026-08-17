def solution(num_list):
    x=1
    xx=0
    for i in num_list:
        x*=i
        xx+=i
    if x< (xx**2):
        return 1
    else:
        return 0