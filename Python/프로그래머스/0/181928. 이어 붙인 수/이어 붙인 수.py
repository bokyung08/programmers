def solution(num_list):
    answer = 0
    odd_sum=''
    even_sum=''
    for i in num_list:
        if i%2==0:
            even_sum+=str(i)
        else:
            odd_sum+=str(i)
    answer=int(even_sum)+int(odd_sum)
    return answer