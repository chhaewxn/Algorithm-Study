def solution(brown, yellow):
    total = brown + yellow

    for width in range(3, int(total**0.5) + 1):
        if total % width == 0:  # 전체 격자 수가 width로 나누어 떨어지는지 확인
            height = total // width
            
            # 노란색 격자 수 계산: (가로-2) × (세로-2)
            yellow_count = (width - 2) * (height - 2)
            
            # 계산된 노란색 격자 수가 주어진 값과 일치하는지 확인
            if yellow_count == yellow:
                # 가로 길이는 세로 길이와 같거나 더 길어야 함
                return [max(width, height), min(width, height)]

    return None
