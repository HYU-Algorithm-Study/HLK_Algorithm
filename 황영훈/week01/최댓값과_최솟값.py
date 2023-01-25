def solution(s):
    answer = ''
    # 문자열을 정수 리스트로 변환
    s = list(map(int, s.split()))
    # 최소값과 최대값 문자열로 반환
    answer = str(min(s)) + " " + str(max(s))
    return answer