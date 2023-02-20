def solution(s):
    answer = 0
    for i in s:
        if i == "(":
            answer += 1
        elif i == ")":
            # )가 먼저 시작한다면 False 리턴
            if answer > 0:
                answer -= 1
            else:
                return False
    
    if answer != 0:
        return False
    else:
        return True