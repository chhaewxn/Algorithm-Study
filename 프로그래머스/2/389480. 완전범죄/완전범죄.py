def solution(info, n, m):
    from functools import lru_cache

    L = len(info)

    @lru_cache(maxsize=None)
    def dfs(i, a_trace, b_trace):
        if a_trace >= n or b_trace >= m:
            return float('inf')  # 실패 케이스
        if i == L:
            return a_trace  # 모든 물건 다 처리함
        
        a_add, b_add = info[i]
        
        # A도둑이 i번 물건 훔침
        take_a = dfs(i + 1, a_trace + a_add, b_trace)
        
        # B도둑이 i번 물건 훔침
        take_b = dfs(i + 1, a_trace, b_trace + b_add)
        
        return min(take_a, take_b)

    result = dfs(0, 0, 0)
    return result if result != float('inf') else -1
