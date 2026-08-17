def solution(n, a, b):
    if a == b:
        return 0

    return 1 + solution(
        n // 2,
        (a + 1) // 2,
        (b + 1) // 2
    )