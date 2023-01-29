def solution(t, p):
    answer = 0
    length = len(p)
    for i, n in enumerate(t):
        substring = t[i:i+length]
        if len(substring) != length:
            return answer
        if int(substring) <= int(p):
            answer += 1
    return answer