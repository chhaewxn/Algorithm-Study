def solution(N, P):
    # 1. 인출 시간이 적은 순서대로 정렬
    P.sort()
    
    # 2. 각 사람이 기다리는 시간의 합을 저장할 변수
    total_waiting_time = 0
    
    # 3. 현재까지의 대기시간을 저장할 변수
    current_time = 0
    
    # 4. 각 사람별로 대기시간 계산
    for time in P:
        # 현재 사람의 인출시간을 더함
        current_time += time
        # 총 대기시간에 현재까지의 대기시간을 더함
        total_waiting_time += current_time
    
    return total_waiting_time