def solution(s):
    parse_list = s.split()
    for i, num in enumerate(parse_list):
        parse_list[i] = int(num)
    max_num = max(parse_list)
    min_num = min(parse_list)
    answer = str(min_num) + " " + str(max_num)
    return answer