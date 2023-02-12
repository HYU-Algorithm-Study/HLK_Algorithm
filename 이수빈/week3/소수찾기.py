import math

prime_numbers = []

def primality(n):
    # 혹은 square_root = n ** 0.5
    square_root = math.sqrt(n)
    
    # n이 2보다 큰 짝수일 경우, 소수가 아니다
    if n != 2 and n % 2 == 0:
        return 0
    
    # n의 제곱근보다 작거나 같은 모든 소수들로 나누어 떨어지지 않으면 n은 소수다
    for i in prime_numbers:
        if i > square_root:
            break
        if i < n and n % i == 0:
            return 0
    
    # 지금까지 찾은 소수 저장
    prime_numbers.append(n)
        
    return 1

def solution(n):
    answer = 0
    for i in range(2, n + 1):
        answer += primality(i)
    
    return answer