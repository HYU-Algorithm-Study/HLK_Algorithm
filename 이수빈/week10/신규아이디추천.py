import re

def solution(new_id):
    new_id = new_id.lower() # 1단계
    
    for character in '~!@#$%^&*()=+[{]}:?,<>/': # 2단계
        new_id = new_id.replace(character, '')
        
    new_id = re.sub('\.(\.)+', '.', new_id) # 3단계
    
    while len(new_id) != 0 and new_id[0] == '.': # 4단계
        new_id = new_id[1:]
    while len(new_id) != 0 and new_id[len(new_id)-1] == '.': 
        new_id = new_id[:-1]

    if new_id == '': # 5단계
        new_id = 'a'

    if len(new_id) >= 16: # 6단계
        new_id = new_id[:15]
        while len(new_id) != 0 and new_id[len(new_id)-1] == '.':
            new_id = new_id[:-1]

    while len(new_id) < 3: # 6단계
        new_id = new_id + new_id[len(new_id) - 1]
        
    answer = new_id
    return answer