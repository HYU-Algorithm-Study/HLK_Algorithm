def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True) # 무게가 무거운 순으로 정렬
    
    begin = 0
    end = len(people) - 1
    while begin <= end:
        if people[begin] > limit - 40 or begin == end: # 혼자서도 무거워서 같이 탈 수 없거나 people에 한 명만 있을 경우
            begin += 1
            answer += 1
        else:
            if people[begin] + people[end] <= limit: # 가장 무거운 사람과 가장 가벼운 사람을 더해서 limit 보다 작으면 둘 다 people에서 빼기
                end -= 1
            begin += 1
            answer += 1
    # while len(people) > 0:
    #     if people[0] > limit - 40 or len(people) == 1:
    #         answer += 1
    #         people.pop(0)
    #     else:
    #         if people[0] + people[-1] <= limit:
    #             people.pop()
    #         people.pop(0)
    #         answer += 1
            
    return answer