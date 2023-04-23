def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 0: # n이 짝수면 점프
            n //= 2
        else: # n이 홀수면 순간 이동
            n -= 1
            answer += 1
            
    return answer