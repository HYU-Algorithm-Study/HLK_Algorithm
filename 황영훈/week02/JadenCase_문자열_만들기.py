def solution(s):
    # 문자열을 소문자 리스트로 변경
    answer = list(s.lower())
    # 첫번째 문자는 대문자
    answer[0] = answer[0].upper()
    # 공백 뒤의 문자는 대문자
    for i in range(len(answer) - 1):
        if answer[i] == ' ':
            answer[i+1] = answer[i+1].upper()
    # 리스트를 문자열로 변경 후 return
    return ''.join(answer)