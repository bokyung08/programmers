def solution(s):
    answer = s.split(" ")
    answer = [i.capitalize() for i in answer]
    return " ".join(answer)