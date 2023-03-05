def solution(n):
    answer = 1 # 자기 자신의 경우도 포함하므로 1로 초기화
    number = 0
    for i in range(n): # 시작하는 숫자
        number += i + 1
        for j in range(i + 2, n): # 시작하는 숫자 + 1부터 n보다 작은 숫자까지
            if number > n: # 지금까지 더한 숫자가 n보다 클 경우 다시 0으로 초기화하고 loop 종료
                number = 0
                break
            number += j
            if number == n: # 지금까지 더한 숫자가 n과 같은 경우 정답 처리
                answer += 1
                number = 0
                break
        
    return answer