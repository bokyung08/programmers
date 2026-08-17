def solution(a, b, c):
    answer = 0
    if a!=b and a!=c and b!=c:
        answer=a+b+c
    if a==b==c:
        answer=(a**3+b**3+c**3)*(a**2+b**2+c**2)*(a+b+c)
    elif a==b or b==c or a==c:
        answer=(a**2+b**2+c**2)*(a+b+c)
        
    return answer