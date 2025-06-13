from itertools import combinations

def solution(n, q, ans):
    count = 0
    # 1부터 n까지의 수 중 5개를 고르는 모든 조합 생성
    for comb in combinations(range(1, n+1), 5):
        is_valid = True
        # 각 시도와 시스템 응답을 확인
        for query, expected in zip(q, ans):
            # comb와 query의 교집합 개수 계산
            if len(set(comb) & set(query)) != expected:
                is_valid = False
                break
        if is_valid:
            count += 1
    return count
