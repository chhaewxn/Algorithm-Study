def solution(sizes):
    # 각 명함을 가로와 세로 중 더 큰 값이 가로로, 작은 값이 세로로 오도록 정렬
    rotated_sizes = []
    for card in sizes:
        # 각 명함을 [큰 값, 작은 값] 형태로 정렬
        rotated_sizes.append(sorted(card, reverse=True))
    
    # 가로 중 최대값, 세로 중 최대값 구하기
    max_width = max(card[0] for card in rotated_sizes)
    max_height = max(card[1] for card in rotated_sizes)
    
    # 최종 지갑 크기 계산
    return max_width * max_height