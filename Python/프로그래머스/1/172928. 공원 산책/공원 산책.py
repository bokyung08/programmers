def solution(park, routes):
    n = len(park)
    m = len(park[0])

    # 시작 위치 찾기
    r, c = 0, 0

    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                r, c = i, j

    # 방향
    direction = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1)
    }

    # 명령 처리
    for route in routes:
        d, dist = route.split()
        dist = int(dist)

        dr, dc = direction[d]

        # 임시 위치
        nr, nc = r, c
        can_move = True

        # 한 칸씩 이동하며 검사
        for _ in range(dist):
            nr += dr
            nc += dc

            # 범위를 벗어난 경우
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                can_move = False
                break

            # 장애물을 만난 경우
            if park[nr][nc] == "X":
                can_move = False
                break

        # 끝까지 이동 가능했다면 실제 위치 갱신
        if can_move:
            r, c = nr, nc

    return [r, c]