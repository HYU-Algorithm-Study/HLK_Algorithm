def solution(n,a,b):
    answer = 1
    if a > b: # a < b로 맞춰주기
        temp = a
        a = b
        b = temp
    
    while True: # 라운드에서 만날 때까지 
        if a % 2 == 1 and b == a + 1: # a가 홀수고 b가 a + 1 이면 둘이 라운드에서 만난 것
            break
            
        if a % 2 == 0:
            a //= 2
        elif a == 1:
            pass
        else:
            a = a // 2 + 1
        
        if b % 2 == 0:
            b //= 2
        else:
            b = b // 2 + 1
        answer += 1
    
    return answer