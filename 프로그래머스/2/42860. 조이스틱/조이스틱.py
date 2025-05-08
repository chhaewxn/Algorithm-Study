def solution(name):
    # 알파벳 변경에 필요한 최소 조작 횟수 계산 함수
    def get_change_count(char):
        up_count = ord(char) - ord('A')
        down_count = ord('Z') - ord(char) + 1
        return min(up_count, down_count)
    
    n = len(name)
    change_count = sum(get_change_count(char) for char in name)
    
    min_move = n - 1  # 오른쪽으로만 이동하는 경우
    
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        forward_then_reverse = i + (n - next_idx) + min(i, n - next_idx)
        min_move = min(min_move, forward_then_reverse)
    
    return change_count + min_move