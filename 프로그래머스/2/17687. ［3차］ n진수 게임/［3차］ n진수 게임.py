def solution(n, t, m, p):
    def convert_to_base_n(num, base):
        if num == 0:
            return '0'
        
        digits = "0123456789ABCDEF"
        result = ""
        
        while num > 0:
            result = digits[num % base] + result
            num //= base
            
        return result
    
    game_str = ''
    num = 0
    
    while len(game_str) < t * m:
        game_str += convert_to_base_n(num, n)
        num += 1
        
    tube_turn = p - 1  # 0-indexed로 변환
    result = ''
    
    for i in range(t):
        result += game_str[tube_turn + i * m]
    
    return result