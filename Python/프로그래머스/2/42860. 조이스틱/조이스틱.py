def solution(name): 
    n = len(name)
    answer=0
    for a in name:
        answer+=min(ord(a)-ord('A'),ord("Z")-ord(a)+1)
    move=n-1
    for i in range(n):
        next=i+1
        while next<n and name[next]=="A":
            next+=1
        back = i+i+(n-next)
        left=(n-next)+(n-next)+i
        move=min(move, back, left)
    return move+answer