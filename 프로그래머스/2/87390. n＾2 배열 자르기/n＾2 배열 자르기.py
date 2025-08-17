def solution(n, left, right):
    # 큰 n 값에 대해서는 전체 배열을 만들지 않고 필요한 값만 계산
    
    # 결과 배열
    result = []
    
    # left부터 right까지만 계산
    for idx in range(left, right + 1):
        # 1차원 인덱스를 2차원 좌표로 변환
        row = idx // n  # 행 번호 
        col = idx % n   # 열 번호 
        
        value = max(row + 1, col + 1)
        result.append(value)
    
    return result