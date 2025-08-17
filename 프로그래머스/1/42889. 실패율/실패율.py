def solution(N, stages):

    # 각 스테이지별 머물러 있는 사용자 수 계산
    stage_counts = [0] * (N + 2)
    for stage in stages:
        stage_counts[stage] += 1
    
    # 각 스테이지별 실패율과 스테이지 번호 계산
    failure_data = []
    total_users = len(stages)
    
    for stage_num in range(1, N + 1):
        stuck_users = stage_counts[stage_num]
        
        # 실패율 계산 (0으로 나누기 방지)
        failure_rate = stuck_users / total_users if total_users > 0 else 0
        
        failure_data.append((failure_rate, stage_num))
        total_users -= stuck_users
    
    # 정렬 후 스테이지 번호만 반환
    failure_data.sort(key=lambda x: (-x[0], x[1]))
    return [stage for rate, stage in failure_data]

