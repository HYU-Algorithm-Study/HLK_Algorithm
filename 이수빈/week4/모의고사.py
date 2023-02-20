def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # answers의 길이까지 a, b, c 늘리기
    length = len(answers)
    while len(a) < length:
        a += a
    while len(b) < length:
        b += b
    while len(c) < length:
        c += c
    
    a_ = a[:length + 1]
    b_ = b[:length + 1]
    c_ = c[:length + 1]
    
    a_answers = 0
    b_answers = 0
    c_answers = 0
    
    # 맞는 문제 수 구하기
    for i in range(length):
        if answers[i] == a_[i]:
            a_answers += 1
        if answers[i] == b_[i]:
            b_answers += 1
        if answers[i] == c_[i]:
            c_answers += 1
    
    max_num = max(a_answers, b_answers, c_answers)
    answer = []
    if a_answers == max_num:
        answer.append(1)
    if b_answers == max_num:
        answer.append(2)
    if c_answers == max_num:
        answer.append(3)
    
    return answer