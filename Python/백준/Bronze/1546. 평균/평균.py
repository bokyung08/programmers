N = int(input())  # 과목 수
scores = list(map(int, input().split()))  # 점수 리스트 입력

max_score = max(scores)  # 최고점
new_scores = [(score / max_score) * 100 for score in scores]  # 점수 조작

average = sum(new_scores) / N  # 평균 계산
print(average)