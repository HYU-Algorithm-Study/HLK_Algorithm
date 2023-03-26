def solution(n, words):
    answer = [0, 0]
    words_len = len(words)
    word_list = []
    turn = 0
    while True:
        for i in range(turn, turn + n): # 번호 순서대로 차례대로 단어 말하기
            if i >= words_len: # index 벗어나면 answer 리턴
                return answer
            current_word = words[i]
            if len(word_list) != 0: # 첫 단어가 아니면
                if word_list[-1][-1] != current_word[0] or current_word in word_list: # 전 단어의 마지막 문자로 시작하지 않거나 이미 나온 문자면 answer 리턴
                    answer[0] = i % n + 1
                    answer[1] = i // n + 1
                    return answer
            word_list.append(current_word) # pass 됐으면 word_list에 단어 추가하기
        turn += n

    return answer