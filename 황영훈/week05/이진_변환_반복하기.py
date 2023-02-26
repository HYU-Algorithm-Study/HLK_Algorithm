def solution(s):
    answer = [0, 0]
    # 이진 변환
    while (s != '1'):
        # 문자열에서 0을 제거
        s = remove_zeros(answer, s)
        # 문자열의 길이를 이진수로 표현
        s = format(len(s), 'b')
        answer[0] += 1
    return answer

def remove_zeros(answer, s):
    new_s = s.replace('0', '')
    answer[1] += len(s) - len(new_s)
    return new_s