def solution(arr):
    answer = []
    a=arr[0]
    answer.append(a)
    for i in arr:     
         if i!=a:
            answer.append(i)
            a=i
    return answer