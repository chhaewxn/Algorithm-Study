from itertools import combinations, product
from collections import Counter

def solution(dice):
    n = len(dice)
    half = n // 2
    
    best_win_rate = 0
    best_combination = []
    
    for a_combo in combinations(range(n), half):
        # B 남은 주사위 가져감
        b_combo = [i for i in range(n) if i not in a_combo]
    
        a_dices = [dice[i] for i in a_combo]
        a_counter = Counter() # Counter로 저장
        for combo in product(*a_dices):
            a_counter[sum(combo)] += 1
        
        b_dices = [dice[i] for i in b_combo]
        b_counter = Counter()
        for combo in product(*b_dices):
            b_counter[sum(combo)] += 1
        
        win_count = 0
        total_cases = sum(a_counter.values()) * sum(b_counter.values())
        
        for a_score, a_freq in a_counter.items():
            for b_score, b_freq in b_counter.items():
                if a_score > b_score:
                    win_count += a_freq * b_freq
    
        win_rate = win_count / total_cases
        
        if win_rate > best_win_rate:
            best_win_rate = win_rate
            best_combination = [i + 1 for i in a_combo]  
    
    return sorted(best_combination)