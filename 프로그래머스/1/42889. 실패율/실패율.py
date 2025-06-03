from collections import Counter

def solution(N, stages):
    
    # 스테이지별 사용자 수 카운트
    stage_count = Counter(stages)
    
    # 실패율 계산 및 정렬
    failure_rates = []
    remaining_users = len(stages)
    
    for stage in range(1, N + 1):
        current_stage_users = stage_count.get(stage, 0)
        
        if remaining_users == 0:
            failure_rate = 0
        else:
            failure_rate = current_stage_users / remaining_users
        
        failure_rates.append((failure_rate, stage))
        remaining_users -= current_stage_users
    
    # 실패율 내림차순, 스테이지 번호 오름차순
    failure_rates.sort(key=lambda x: (-x[0], x[1]))
    
    return [stage for _, stage in failure_rates]