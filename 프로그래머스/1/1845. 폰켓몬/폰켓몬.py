def solution(nums):
    # 가져갈 수 있는 폰켓몬 수: N/2
    pick_count = len(nums) // 2
    
    # 폰켓몬 종류의 수 계산
    pokemon_types = set(nums)
    type_count = len(pokemon_types)
    
    # 종류의 수와 가져갈 수 있는 폰켓몬 수 중 작은 값 반환
    return min(type_count, pick_count)