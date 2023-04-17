def solution(ingredient):
    answer = 0
    
    st = [] # stack
    for i in ingredient:
        st.append(i) # put an ingredient
        if len(st) >= 4: # if there are more than 4 ingredients
            if st[-1] == 1 and st[-2] == 3 and st[-3] == 2 and st[-4] == 1:
                answer += 1 # plus one to answer if it suits a condition
                # st = st[:-4] # time over
                for j in range(4):
                    st.pop() # remove four ingredients
    
    return answer