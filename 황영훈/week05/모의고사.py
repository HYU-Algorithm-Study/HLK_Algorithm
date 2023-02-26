def solution(answers):
    answer = []
    # 수포자들의 점수
    scores = [0, 0, 0]
    # 수포자들의 찍기 방식
    types = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
             [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    # 정답을 맞춘 수포자는 1점 획득
    for i in range(len(answers)):
        for j in range(3):
            # 찍기 방식이 순환되도록 % 연산 사용
            if answers[i] == types[j][i % len(types[j])]:
                scores[j] += 1
    # 점수가 최대인 모든 수포자를 리스트에 추가
    for j in range(3):
        if scores[j] == max(scores):
            answer.append(j + 1)
    return answer