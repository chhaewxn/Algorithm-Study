def solution(s):
    stack = []
    
    for char in s:
        if char == '(':  # 여는 괄호면 스택에 추가
            stack.append(char)
        else:  # 닫는 괄호인 경우
            # 스택이 비어있으면 짝이 맞지 않음
            if not stack:
                return False
            # 스택에서 여는 괄호 하나 제거
            stack.pop()
    
    # 모든 문자를 처리한 후 스택이 비어있어야 모든 괄호의 짝이 맞음
    return len(stack) == 0