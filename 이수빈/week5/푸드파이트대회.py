def solution(food):
    answer = ''
    for i in range(len(food)):
        # 0번째 음식 (물)이 아닌 경우, 음식의 개수가 홀수이면 짝수로 맞춰주기
        if food[i] % 2 != 0 and i != 0:
            food[i] -= 1
    for j in range(len(food)):
        # 음식 나열하기
        if food[j] > 0 and j != 0:
            answer += str(j) * (food[j] // 2)
    answer = answer + "0" + answer[::-1]
            
    return answer