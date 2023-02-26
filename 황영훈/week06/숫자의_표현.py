def solution(n):
    answer = 0
    # 연속한 자연수의 시작점 i
    for i in range(1, n + 1):
        # 연속한 자연수의 합 temp
        temp = 0
        # 연속한 자연수의 합이 n과 같아지면 정답
        while temp < n:
            temp += i
            if temp == n:
                answer += 1
            i += 1
    return answer