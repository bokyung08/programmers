def solution(s):
    cnt =0
    a=0
    n=0
    while len(s)!=1:
        cnt=0
        for i in s: 
            if i=='1':
                cnt+=1
            else:
                a+=1
                continue
        s=bin(cnt)[2:]
        n+=1
    return [n, a]