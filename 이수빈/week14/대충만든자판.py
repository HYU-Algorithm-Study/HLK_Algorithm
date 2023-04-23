def solution(keymap, targets):
    answer = []
    
    for target in targets:
        total = 0
        for character in target: # target의 한 글자씩 돌면서 keymap을 몇 번 눌러야 입력할 수 있는지 확인
            location = 101
            for key in keymap:
                if character in key:
                    location = min(location, key.find(character) + 1) # 위치의 최솟값
            total += location
            if location == 101: # 찾지 못했으면 -1
                total = 101
                break
        if total == 101:
            total = -1
        answer.append(total)
    
    return answer