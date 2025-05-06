def solution(s):
    def is_valid(string):
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}
        
        for char in string:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack.pop() != brackets[char]:
                    return False
        
        return len(stack) == 0
    
    length = len(s)
    count = 0
    
    for i in range(length):
        # 문자열을 i만큼 왼쪽으로 회전
        rotated = s[i:] + s[:i]
        
        if is_valid(rotated):
            count += 1
    
    return count