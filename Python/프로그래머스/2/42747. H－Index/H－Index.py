def solution(citations):
    citations = sorted(citations)

    for idx, num in enumerate(citations):
        h = len(citations) - idx

        if num >= h:
            return h

    return 0