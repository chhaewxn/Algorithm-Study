from collections import deque

def solution(priorities, location):
    # 프로세스 정보를 (우선순위, 원래 위치) 형태로 큐에 저장
    queue = deque([(p, idx) for idx, p in enumerate(priorities)])
    
    # 실행 순서 카운트
    execution_order = 0
    
    while queue:
        # 현재 프로세스를 큐에서 꺼냄
        current = queue.popleft()
        
        # 큐에 남아있는 프로세스 중 우선순위가 더 높은 프로세스가 있는지 확인
        if any(current[0] < q[0] for q in queue):
            # 우선순위가 더 높은 프로세스가, 있으면 현재 프로세스를 큐의 맨 뒤에 다시 삽입
            queue.append(current)
        else:
            # 현재 프로세스 실행
            execution_order += 1
            
            # 찾고자 하는 프로세스인지 확인
            if current[1] == location:
                return execution_order