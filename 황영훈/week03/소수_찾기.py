def solution(n):
    answer = 0
    # 검사할 정수 리스트 생성
    nums = [num for num in range(2, n + 1)]
    # 소수면 정답에 추가
    for num in nums:
        if is_prime(num):
            answer += 1
    return answer

def is_prime(n):
    # 시간 효율을 위해 제곱근까지만 검사
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True