def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    matched_count = len(set(lottos) & set(win_nums))
    
    def get_rank(count):
        return 7 - count if count >= 2 else 6

    max_rank = get_rank(matched_count + zero_count)
    min_rank = get_rank(matched_count)
    
    return [max_rank, min_rank]
