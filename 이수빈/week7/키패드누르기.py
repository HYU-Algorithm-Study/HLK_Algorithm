def solution(numbers, hand):
    answer = ""
    l = 10 # 왼손의 위치
    r = 11 # 오른손의 위치
    # 각 숫자의 위치 값 저장
    number_pad = [[3, 1], 
                  [0, 0], [0, 1], [0, 2], 
                  [1, 0], [1, 1], [1, 2], 
                  [2, 0], [2, 1], [2, 2], 
                  [3, 0], [3, 2]]
    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            l = n
        elif n in [3, 6, 9]:
            answer += "R"
            r = n
        else: # 2, 5, 8, 0 중 하나일 경우 맨해튼 거리 (|x1−x2|+|y1−y2|)를 구하여 둘 중 짧은 쪽을 택한다
            l_dist = abs(number_pad[l][0] - number_pad[n][0]) + abs(number_pad[l][1] - number_pad[n][1])
            r_dist = abs(number_pad[r][0] - number_pad[n][0]) + abs(number_pad[r][1] - number_pad[n][1])
            if l_dist < r_dist:
                answer += "L"
                l = n
            elif l_dist > r_dist:
                answer += "R"
                r = n
            else:
                if hand == "left":
                    answer += "L"
                    l = n
                else:
                    answer += "R"
                    r = n
            
    return answer