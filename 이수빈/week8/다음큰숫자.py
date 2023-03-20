def solution(n):
    answer = 0
    bin_n = '0' + bin(n)[2:] # 맨 처음에 1이 나오는 케이스를 대비하기 위해 0을 더한다
    list_bin = list(map(int, bin_n))
    num_one = 0
    for i in range(len(bin_n) - 1, 0, -1):
        if list_bin[i] == 1 and list_bin[i - 1] == 0: # 뒤에서부터 돌면서 왼쪽에 0이 나오는 1을 찾고, 둘을 swap한다
            list_bin[i] = 0
            list_bin[i - 1] = 1
            break
        else:
            num_one += list_bin[i] # 1이 나온 개수를 저장한다
            list_bin[i] = 0 # 지나온 자리를 0으로 변경한다
    for j in range(num_one):
        list_bin[-j-1] = 1 # 1의 개수만큼 뒤에서부터 1을 넣는다
    
    n = 0
    for k in range(len(list_bin)): # 이진수를 십진수로 변환한다
        if list_bin[-k-1] == 1:
            answer += pow(2, n)
        n += 1
        
    # bin_s = ''.join(map(str, list_bin)) # string으로 만든 후
    # answer = int(bin_s, 2) # binary를 decimal로 변환한다
    return answer