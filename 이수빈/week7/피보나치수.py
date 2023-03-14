def fibo(n):
    numbers = [0, 1] # numbers에 계산한 결과 값들 저장장
    if n >= 2:
        for i in range(n - 1): # n - 1번 만큼 반복해 새로운 수 계산
            new = numbers[-1] + numbers[-2]
            numbers.append(new)
    return numbers[-1]
def solution(n):
    answer = fibo(n) % 1234567
    return answer