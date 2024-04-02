def solution(arr, n):
    answer = []
    if len(arr)%2!=0:
        for i in range(0,len(arr),1):
            if i%2==0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
    else:
        for i in range(0,len(arr),1):
            if i%2==0:
                answer.append(arr[i])
            else:
                answer.append(arr[i]+n)    
    return answer