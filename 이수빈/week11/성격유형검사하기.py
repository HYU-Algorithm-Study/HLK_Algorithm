def solution(survey, choices):
    answer = ''
    score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0} # 점수 담는 dictionary
    
    for i in range(len(survey)):
        disagree_type = survey[i][0] # 비동의 관련 선택지를 선택하면 받는 성격 유형
        agree_type = survey[i][1] # 동의 관련 선택지를 선택하면 받는 성격 유형
        choice = choices[i]
        
        if choice == 1:
            score[disagree_type] += 3
        elif choice == 2:
            score[disagree_type] += 2
        elif choice == 3:
            score[disagree_type] += 1
        elif choice == 5:
            score[agree_type] += 1
        elif choice == 6:
            score[agree_type] += 2
        elif choice == 7:
            score[agree_type] += 3
    
    if score['R'] < score['T']:
        answer += 'T'
    else:
        answer += 'R'
    if score['C'] < score['F']:
        answer += 'F'
    else:
        answer += 'C'
    if score['J'] < score['M']:
        answer += 'M'
    else:
        answer += 'J'
    if score['A'] < score['N']:
        answer += 'N'
    else:
        answer += 'A'
            
    return answer