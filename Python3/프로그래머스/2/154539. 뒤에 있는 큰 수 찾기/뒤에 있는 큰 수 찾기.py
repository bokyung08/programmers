def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            previous_idx = stack.pop()
            answer[previous_idx] = num

        stack.append(idx)

    return answer