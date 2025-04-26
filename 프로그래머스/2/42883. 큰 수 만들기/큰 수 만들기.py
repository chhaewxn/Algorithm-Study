def solution(number, k):
    stack = []

    for digit in number:
        # 스택이 비어있지 않고 k가 0보다 크고 맨위 숫자가 현재 숫자보다 작으면 제거
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        
        stack.append(digit)
        
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)