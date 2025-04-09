import math

def solution(progresses, speeds):
    days_required = []
    for progress, speed in zip(progresses, speeds):
        days = math.ceil((100 - progress) / speed)
        days_required.append(days)
    
    result = []
    deploy_day = days_required[0]
    count = 1
    
    for i in range(1, len(days_required)):
        if days_required[i] > deploy_day:
            result.append(count)
            # 새로운 배포일 설정
            deploy_day = days_required[i]
            # 새 배포일에 배포될 기능 수 초기화
            count = 1
        else:
            count += 1
    
    # 마지막 배포 그룹 추가
    result.append(count)
    
    return result