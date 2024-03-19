def solution(numbers):
    answer = 0
    li=[0,1,2,3,4,5,6,7,8,9]
    for i in range(len(numbers)):
        if numbers[i] in li:
            li.remove(numbers[i])
    for i in li:
        answer+=i
    return answer