def solution(clothes):
    # 의상 종류별로 개수를 저장할 딕셔너리
    clothes_type_count = {}
    
    # 의상 종류별 개수 계산
    for name, category in clothes:
        if category in clothes_type_count:
            clothes_type_count[category] += 1
        else:
            clothes_type_count[category] = 1
    
    # 조합 계산: (각 종류별 의상 개수 + 1)을 모두 곱한 후 1을 빼기
    # +1은 해당 종류의 의상을 입지 않는 경우를 포함
    # 마지막에 -1은 모든 종류의 의상을 입지 않는 경우를 제외
    result = 1
    for count in clothes_type_count.values():
        result *= (count + 1)
    
    # 아무것도 입지 않는 경우를 제외
    return result - 1