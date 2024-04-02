def solution(arr1, arr2):
    sum1=0
    sum2=0
    if len(arr1)!=len(arr2):
        if len(arr1)>len(arr2):
            return 1
        else:
            return -1
    else:
        for i in arr1:
            sum1+=i
        for j in arr2:
            sum2+=j
        if sum1!=sum2:
            if sum1>sum2:
                return 1
            else:
                return -1
        else:
            return 0    
