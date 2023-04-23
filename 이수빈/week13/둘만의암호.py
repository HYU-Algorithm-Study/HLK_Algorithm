import string
def solution(s, skip, index):
    answer = ''
    lower_alphabet = string.ascii_lowercase
    for skip_letter in skip:
        lower_alphabet = lower_alphabet.replace(skip_letter, '') # 소문자들에서 skip에 있는 것 빼기
    
    for letter in s:
        answer += lower_alphabet[(lower_alphabet.find(letter) + index) % len(lower_alphabet)] # skip에 없는 문자들 중에서 index 만큼 뒤에 있는 알파벳 찾기
    
    return answer