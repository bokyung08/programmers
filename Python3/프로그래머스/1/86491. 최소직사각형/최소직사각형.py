def solution(sizes):
    max_w=max_h=0
    for i in sizes:
        wid,hei=i
        max_w=max(max_w,wid,hei)
        max_h=max(max_h,min(hei,wid))
                
    return max_h*max_w