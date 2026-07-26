from collections import deque

def solution(s):
    s = deque(s)
    answer = 0

    for _ in range(len(s)):
        stack = []
        is_valid = True

        for char in s:
            if char in "([{":
                stack.append(char)

            else:
                # 닫는 괄호인데 대응할 여는 괄호가 없는 경우
                if not stack:
                    is_valid = False
                    break

                top = stack.pop()

                if char == ")" and top != "(":
                    is_valid = False
                    break
                elif char == "]" and top != "[":
                    is_valid = False
                    break
                elif char == "}" and top != "{":
                    is_valid = False
                    break

        # 검사 종료 후 여는 괄호가 남아 있으면 잘못된 문자열
        if is_valid and not stack:
            answer += 1

        # 문자열을 왼쪽으로 한 칸 회전
        s.append(s.popleft())

    return answer