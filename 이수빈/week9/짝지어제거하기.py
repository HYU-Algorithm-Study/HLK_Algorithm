def solution(s):
    answer = 1
    st = [] # stack
    
    for i in range(len(s)):
        if len(st) and st[-1] == s[i]: # 마지막 원소가 s[i]인 경우 마지막 원소 제거
            st.pop()
        else:
            st.append(s[i]) # 그렇지 않은 경우 스택에 원소 삽입
            
    if len(st): # 스택에 원소가 남아있으면 짝지어 제거하기 실패
        answer = 0
    return answer