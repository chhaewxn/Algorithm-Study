from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)  # 귤 크기별 개수 카운팅
    sorted_counts = sorted(counter.values(), reverse=True)  # 많이 있는 크기부터 정렬
    
    count = 0  # 누적 개수
    types = 0  # 사용된 귤 종류 

    for c in sorted_counts:
        count += c
        types += 1
        if count >= k:
            return types
