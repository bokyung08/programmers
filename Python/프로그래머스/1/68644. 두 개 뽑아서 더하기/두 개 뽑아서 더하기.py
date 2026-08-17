def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j:
                a=numbers[i]+numbers[j]
                if a not in answer:
                    answer.append(a)
    return sorted(answer)