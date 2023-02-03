def solution(s):
    s = s.lower()
    answer = ''
    for i in s:
        if answer == '' or answer[-1] == ' ':
            answer += i.upper()
        else:
            answer += i
    return answer