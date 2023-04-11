def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0: # 약수이면
            side_a = i # 노란색 격자의 한 측면
            side_b = yellow // i # 노란색 격자의 다른 측면
            side_a_brown = side_a + 2 # 갈색 격자의 한 측면
            side_b_brown = side_b + 2 # 갈색 격자의 다른 측면
            if side_a_brown * side_b_brown == brown + yellow: # 갈색의 테두리가 한 줄이면
                answer.append(side_a_brown)
                answer.append(side_b_brown)
                break
    answer = sorted(answer, reverse=True)
    return answer