def solution(ingredient):
    answer = 0
    ham = [1, 2, 3, 1]
    stack = []

    for i in ingredient:
        stack.append(i)
        if stack[-4:] == ham:  # 마지막 4개가 ham과 동일한 경우
            answer += 1
            del stack[-4:]  # 해당 부분 제거

    return answer