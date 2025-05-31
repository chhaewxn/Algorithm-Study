def solution(s):
    transform_count = 0  
    removed_zeros = 0   
    
    # "1"이 될 때까지 반복
    while s != "1":
        zero_count = s.count('0')
        removed_zeros += zero_count

        s = s.replace('0', '')
        
        length = len(s)
        s = bin(length)[2:]  # bin()의 '0b' 접두사 제거
        
        # 변환 횟수 증가
        transform_count += 1
    
    return [transform_count, removed_zeros]