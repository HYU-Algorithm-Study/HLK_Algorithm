def solution(board, moves):
    answer = 0
    data_list = []
    answer_list = []
    board_len = len(board[0])
    
    for i in range(board_len):
        block = [] # 1번부터 N번 칸까지
        for j in range(len(board) - 1, -1, -1):
            if board[j][i] != 0:
                block.append(board[j][i]) # 각 칸의 스택 쌓기 (데이터 변형)
        data_list.append(block)
            
    for j in moves:
        if len(data_list[j - 1]) == 0: # 칸에 인형이 아무 것도 없으면 아무 일도 일어나지 않는다
            continue

        block_data = data_list[j - 1][-1]
        data_list[j - 1].pop()
        
        if len(answer_list) != 0:
            if answer_list[-1] == block_data: # 맨 위와 같은 인형이 들어가면 터뜨려진다
                answer_list.pop()
                answer += 2
                continue
        answer_list.append(block_data)
            
    return answer