def solution(s):
    # 문자열 파싱 및 집합 크기순 정렬
    s = s.replace('{{', '').replace('}}', '').split('},{')
    parsed_sets = []
    
    for subset in s:
        nums = [int(num) for num in subset.split(',')]
        parsed_sets.append(set(nums))
    
    parsed_sets.sort(key=len)
    
    # 튜플 복원
    result = []
    prev_set = set()
    
    for current_set in parsed_sets:
        # 차집합에서 새로운 원소 추출
        new_elem = list(current_set - prev_set)[0]
        result.append(new_elem)
        prev_set = current_set
    
    return result