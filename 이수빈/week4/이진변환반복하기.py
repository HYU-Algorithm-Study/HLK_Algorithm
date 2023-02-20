def solution(s):
    answer = []
    a = 0
    b = 0

    # s가 1이 될 때까지 반복
    while s != "1":
        # s에서 0의 개수 세고, 0을 빼고 남은 1들을 after_reduce에 저장
        zero = s.count("0")
        after_reduce = len(s) - zero

        # after_reduce를 이진숫자로 변환 (0b 없애기 위해 2번째부터 저장)
        s = bin(after_reduce)[2:]
        a += 1
        b += zero
    answer = [a, b]
    return answer

solution("110010101001")