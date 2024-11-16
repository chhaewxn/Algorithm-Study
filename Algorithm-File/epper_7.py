def solution(s):
    answer = 0  # 총 점수를 저장할 변수
    current_score = 0  # 연속 점수를 계산할 변수

    # 문자열의 각 문자에 대해 점수 계산
    for char in s:
        if char == 'O':  # 맞춘 경우
            current_score += 1  # 연속 점수 증가
            answer += current_score  # 총 점수에 추가
        else:  # 틀린 경우
            current_score = 0  # 연속 점수 초기화

    return answer