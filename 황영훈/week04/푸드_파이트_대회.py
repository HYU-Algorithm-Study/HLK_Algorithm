def solution(food):
    # 한 선수가 먹을 음식 양을 계산
    food = [x // 2 for x in food]
    order = ''
    for i in range(len(food)):
        # 음식을 순서대로 배치
        order += str(i) * food[i]
    # 대회를 위한 음식 배치
    return order + '0' + order[::-1]