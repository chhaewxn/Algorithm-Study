def solution(bandage, health, attacks):
    # 초기 설정
    max_health = health  # 최대 체력 저장
    current_health = health  # 현재 체력
    casting_time, healing, bonus = bandage  # 붕대 감기 속성
    last_attack_time = attacks[-1][0]  # 마지막 공격 시간
    
    # 공격 시간을 딕셔너리로 변환 (빠른 검색을 위해)
    attack_dict = {time: damage for time, damage in attacks}
    
    # 연속 성공 횟수
    success_streak = 0
    
    # 1초부터 마지막 공격 시간까지 진행
    for current_time in range
    (1, last_attack_time + 1):
        # 1. 공격이 있는 경우
        if current_time in attack_dict:
            current_health -= attack_dict[current_time]  # 체력 감소
            success_streak = 0  # 연속 성공 초기화
            
            # 체력이 0 이하가 되면 -1 반환
            if current_health <= 0:
                return -1
                
        # 2. 공격이 없는 경우 - 붕대 감기
        else:
            # 기본 회복량 적용
            current_health += healing
            success_streak += 1
            
            # 연속 성공 보너스 체크
            if success_streak == casting_time:
                current_health += bonus  # 추가 회복
                success_streak = 0  # 연속 성공 초기화
            
            # 최대 체력 초과 검사
            current_health = min(current_health, max_health)
    
    return current_health
