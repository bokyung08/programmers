def solution(babbling):
    answer = 0
    for word in babbling:
        temp = word
        for s in ["aya", "ye", "woo", "ma"]:
            if s * 2 in temp:   # 같은 발음 2번 연속이면
                continue        # 이 발음은 치환하지 않음 → 나중에 글자 남음
            temp = temp.replace(s, " ")
        if temp.strip() == "":
            answer += 1
    return answer