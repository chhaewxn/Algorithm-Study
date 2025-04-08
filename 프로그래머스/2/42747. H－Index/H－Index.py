def solution(citations):
    # 인용 횟수를 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # H-Index 계산
    answer = 0
    for i, citation in enumerate(citations):
        # 현재 논문이 i+1번째 논문이고, 인용 횟수가 i+1 이상인지 확인
        # (i+1은 현재까지 고려한 논문의 수)
        if citation >= i + 1:
            answer = i + 1
        else:
            break
    
    return answer