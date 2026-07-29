def solution(players, callings):
    # 이름 -> 현재 인덱스(등수-1) 매핑
    index_of = {name: i for i, name in enumerate(players)}

    for called in callings:
        i = index_of[called]        # 불린 선수의 현재 위치
        front = i - 1               # 바로 앞 선수의 위치
        front_name = players[front]

        # 두 선수의 자리를 교환 (추월)
        players[i], players[front] = players[front], players[i]

        # 매핑 갱신
        index_of[called] = front
        index_of[front_name] = i

    return players