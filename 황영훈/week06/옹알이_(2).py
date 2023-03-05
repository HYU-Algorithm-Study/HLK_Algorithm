def solution(babbling):
    answer = 0
    # 옹알이 리스트에 가능한 옹알이가 있을 때마다 정답 1씩 증가
    for b in babbling:
        answer += int(is_enabled(b))
    return answer

# 가능한 옹알이인지 판단하는 함수
def is_enabled(b):
    # 가능한 패턴
    pattern = ["aya", "ye", "woo", "ma"]
    # 불가능한 패턴
    anti_pattern = [p * 2 for p in pattern]
    # 불가능한 패턴이 있으면 return False
    for p in anti_pattern:
        if p in b:
            return False
    # 패턴에 해당하는 단어를 공백으로 대체
    # 공백으로 대체해야 새로운 단어가 형성되지 않음
    # EX) mayaa -> m a
    for p in pattern:
        b = b.replace(p, " ")
    b = b.replace(" ", "")
    # 패턴에 해당하는 단어만 있으면 True 그렇지 않으면 False
    return True if b == "" else False