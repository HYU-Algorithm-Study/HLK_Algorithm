def solution(s):
    s = s.lower()
    s = s.replace('  ', ' ')
    words = s.split()
    answer = ''
    for word in words:
        new_word = word.replace(word[0], word[0].upper())
        answer += new_word
        answer += ' '
    answer = answer[:-1]
    return answer