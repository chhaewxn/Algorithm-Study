def solution(n):
    # n × n 크기의 2차원 배열을 생성하고 모든 값 0으로 초기화
    # 외부 리스트는 행을 나타내고, 내부 리스트는 각 행의 열
    arr = []
    
    # n개의 행을 생성
    for i in range(n):
        # 각 행마다 n개의 0으로 채워진 리스트를 생성
        row = []
        for j in range(n):
            # 모든 위치에 일단 0 넣기
            row.append(0)
        
        # 완성된 행을 전체 배열에 추가
        arr.append(row)
    
    # 대각선 위치 (i == j인 위치)에만 1을 할당
    for i in range(n):
        # i번째 행의 i번째 열에 1을 할당 
        # arr[i][i] = 1 은 i번째 행의 i번째 열
        arr[i][i] = 1
    
    return arr
