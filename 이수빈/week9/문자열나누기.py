def solution(s):
    answer = 0
    is_x = 1 # x와 같은 글자의 수
    is_not_x = 0 # x와 다른 글자의 수
    x = s[0] # 첫 글자
    for i in range(1, len(s)):
        if s[i] == x:
            is_x += 1
        else:
            is_not_x += 1
        
        if is_x == is_not_x:
            answer += 1
            is_x = 0
            is_not_x = 0
            if i < len(s) - 1:
                x = s[i + 1]
                
    if is_x or is_not_x: # 남아있는 글자가 있으면 분리해주기
        answer += 1
    
    return answer