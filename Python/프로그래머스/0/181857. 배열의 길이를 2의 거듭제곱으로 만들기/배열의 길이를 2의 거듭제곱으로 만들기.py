def solution(arr):
    n=len(arr)
    l=[1,2,4,8,16,32,64,128,256,512,1024]
    if n in l:
        return arr
    
    while True:
        arr.append(0)
        n=len(arr)
        if n in l:
            return arr