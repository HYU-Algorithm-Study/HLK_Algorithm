def solution(t, p):
    answer = 0
    # 문자열 t를 끝까지 검사하도록 범위 설정
    for i in range(len(t) - len(p) + 1):
        # 슬라이싱한 문자열이 p보다 작으면 answer에 추가
        if int(p) >= int(t[i:i+len(p)]):
            answer += 1
    return answer