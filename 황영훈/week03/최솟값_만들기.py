def solution(A,B):
    # 두 수의 곱의 합이 최소가 되려면 큰 수와 작은 수를 곱해야 한다.
    A.sort()
    B.sort(reverse=True)
    result = 0
    for i in range(len(B)):
        result += A[i] * B[i]
    return result