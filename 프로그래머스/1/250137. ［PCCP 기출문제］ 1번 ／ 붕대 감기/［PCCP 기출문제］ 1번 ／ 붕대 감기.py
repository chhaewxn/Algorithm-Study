def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    attack_dict = {time: damage for time, damage in attacks}
    
    current_health = health
    success_time = 0
    
    last_attack_time = attacks[-1][0]
    
    for time in range(1, last_attack_time + 1):
        if time in attack_dict:
            # 공격 받음
            current_health -= attack_dict[time]
            if current_health <= 0:
                return -1
            success_time = 0  # 연속 성공 초기화
        else:
            # 회복
            current_health += x
            success_time += 1
            if success_time == t:
                current_health += y
                success_time = 0  # 다시 초기화
            current_health = min(current_health, max_health)
    
    return current_health
