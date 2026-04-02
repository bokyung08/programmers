def solution(n):
    n1=bin(n)[2:]
    cnt1=0
    for i in n1:
        if i=="1":
            cnt1+=1
        else:
            continue
    print(cnt1)
    for i in range(n+1,1000000,1):
            cnt2=0
            n2=bin(i)[2:]
            for j in n2:
                if j=="1":
                    cnt2+=1
                else:
                    continue
            if cnt1==cnt2:
                break
    return int(n2,2)