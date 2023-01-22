def solution(a, b, n):
    answer = 0
    # 빈 병을 콜라로 교환
    while n >= a:
        # 교환한 콜라 개수를 정답에 추가
        answer += (n // a) * b
        # 빈 병 = 교환한 콜라 + 남은 빈 병
        n = (n // a) * b + (n % a)
    return answer