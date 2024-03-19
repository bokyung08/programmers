def solution(absolutes, signs):
    ab=[]
    s=0
    for i in range(len(signs)):
        if signs[i]==False:
            ab.append(int(absolutes[i]*-1))
        else:
            ab.append(absolutes[i])
    for u in ab:
        s+=u
        
    return s