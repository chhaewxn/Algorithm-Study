def solution(n, left, right):
    result = []
    
    # left부터 right까지의 위치에 해당하는 값만 계산
    for i in range(left, right + 1):
        row = i // n  
        col = i % n   
        
        # (row, col) 위치의 값은 max(row, col) + 1
        # 왜냐면 i행 i열까지는 i로 채워지기 때문
        value = max(row, col) + 1
        result.append(value)
    
    return result