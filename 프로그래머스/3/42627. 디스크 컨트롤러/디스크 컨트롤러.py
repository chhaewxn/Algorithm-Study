import heapq

def solution(jobs):
    # 작업 요청 시간 순으로 정렬
    jobs.sort()
    
    # 작업 번호 부여 (0번부터)
    jobs_with_index = [(i, start, duration) for i, (start, duration) in enumerate(jobs)]
    
    n = len(jobs)  # 전체 작업 수
    current_time = 0  # 현재 시간
    total_turnaround_time = 0  # 전체 반환 시간
    
    # 대기 큐
    waiting_queue = []
    job_index = 0  # 다음에 처리할 작업 인덱스
    
    # 모든 작업이 처리될 때까지 반복
    while job_index < n or waiting_queue:
        # 현재 시간까지 들어온 모든 작업을 대기 큐에 추가
        while job_index < n and jobs_with_index[job_index][1] <= current_time:
            idx, start, duration = jobs_with_index[job_index]
            # 소요시간, 요청시각, 작업번호 순으로 우선순위 (소요시간이 짧은 순)
            heapq.heappush(waiting_queue, (duration, start, idx))
            job_index += 1
        
        # 대기 큐가 비어있다면 다음 작업 요청 시간으로 시간 이동
        if not waiting_queue:
            current_time = jobs_with_index[job_index][1]
            continue
        
        # 우선순위가 가장 높은 작업 선택
        duration, start, idx = heapq.heappop(waiting_queue)
        
        # 작업 수행
        current_time += duration
        
        # 반환 시간 계산 및 누적
        turnaround_time = current_time - start
        total_turnaround_time += turnaround_time
    
    return total_turnaround_time // n