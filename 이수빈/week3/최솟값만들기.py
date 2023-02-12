def solution(A,B):
    answer = 0
    # A와 B 정렬 (각각 오름차순, 내림차순으로)
    A = sorted(A)
    B = sorted(B, reverse=True)

    # A에서 작은 숫자가 B에서의 큰 숫자와 곱해지도록 계산 
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer