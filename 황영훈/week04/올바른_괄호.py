def solution(brackets):
    # stack 활용
    stack = []
    for bracket in brackets:
        # push
        if bracket == '(':
            stack.append(bracket)
        # pop
        else:
            if len(stack) == 0 or stack.pop() == ')':
                return False
    # stack이 비어있지 않으면, 괄호 짝이 안 맞는 것
    return True if len(stack) == 0 else False