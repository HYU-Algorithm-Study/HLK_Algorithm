import re

def solution(babbling):
    answer = 0
    p1 = re.compile(r'\b(aya|ye|woo|ma)+\b') # 해당하는 단어가 1번 이상 나오는 패턴
    p2 = re.compile(r'(aya){2,}|(ye){2,}|(woo){2,}|(ma){2,}') # 해당하는 단어가 연속적으로 2번 이상 나오는 패턴
    for word in babbling:
        if p1.search(word) and not p2.search(word): # 패턴1에는 맞지만, 패턴2에는 맞지 않는 경우
            answer += 1
    
    return answer