a = int(input())  # 단어 개수 입력
cnt = 0  # 그룹 단어 개수

for _ in range(a):
    word = input()  # 단어 입력
    seen = set()  # 이미 등장한 문자 저장
    prev = ''  # 이전 문자 저장
    is_group_word = True  # 그룹 단어 여부

    for char in word:
        if char in seen and char != prev:  # 이전에 나온 문자가 다른 위치에서 다시 등장하면 그룹 단어 X
            is_group_word = False
            break
        seen.add(char)  # 현재 문자 추가
        prev = char  # 이전 문자 갱신

    if is_group_word:
        cnt += 1  # 그룹 단어 개수 증가

print(cnt)
