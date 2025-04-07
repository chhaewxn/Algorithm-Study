def solution(numbers):
    str_numbers = list(map(str, numbers))
    
    # 문자열 비교 함수 정의 (x+y와 y+x를 비교)
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 정렬된 숫자들을 이어붙이기
    answer = ''.join(str_numbers)
    
    # 결과가 '0'으로만 이루어진 경우(ex: [0,0,0]) '0'을 반환
    return '0' if answer[0] == '0' else answer