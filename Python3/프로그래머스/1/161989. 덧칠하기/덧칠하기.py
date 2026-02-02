def solution(n, m, section):
    answer = 0
    if max(section) - min(section) < m - 1:
        return 1

    li = [1] * n
    for i in section:
        li[i - 1] = 0  # 1-based to 0-based index 변환

    i = 0
    while i < n:
        if li[i] == 0:
            answer += 1
            for j in range(i, min(i + m, n)):
                li[j] = 1  # 실제 li의 값을 갱신
            i += m  # 이미 칠한 부분은 건너뜀
        else:
            i += 1

    return answer
