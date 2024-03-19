def solution(price, money, count):
    RealPrice=0
    for i in range(0,count+1,1):
        RealPrice+=i*price
    if RealPrice>money:
        answer=RealPrice-money
    else:
        answer=0
    return answer