def solution(word):
    # 모음과 각 자리수별 가중치를 정의
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    # 각 자리수별 가중치 계산
    weights = [781, 156, 31, 6, 1]
    
    # 순서 계산
    order = 0
    for i, char in enumerate(word):
        vowel_index = vowels.index(char)
        order += vowel_index * weights[i] + 1
    
    return order