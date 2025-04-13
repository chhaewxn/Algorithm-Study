def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],  # 1번 수포자
        [2, 1, 2, 3, 2, 4, 2, 5],  # 2번 수포자
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 3번 수포자
    ]
    
    # 각 수포자별 정답 수를 저장할 리스트
    scores = [0, 0, 0]
    
    # 각 문제에 대해 수포자들의 답과 정답 비교
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            # 패턴의 길이로 나눈 나머지를 이용하여 현재 문제에 대한 각 수포자의 답 확인
            if pattern[i % len(pattern)] == answer:
                scores[j] += 1
    
    # 최고 점수 찾기
    max_score = max(scores)
    
    # 최고 점수를 받은 사람들 (인덱스는 0부터 시작하므로 1을 더해줌)
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]
    
    return result