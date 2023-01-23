def solution(a, b, n):
    answer = 0
    remaining_bottle = 0
    while (n >= a):
        if (n % a) == 0:
            n = (n // a) * b
            answer += n
            if remaining_bottle > 0:
                n += remaining_bottle
                remaining_bottle = 0
        else:
            remaining_bottle += n % a
            n -= n % a
            n = (n // a) * b
            answer += n
            if remaining_bottle > 0:
                n += remaining_bottle
                remaining_bottle = 0
    return answer