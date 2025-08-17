def solution(answers):
    
    # 각 수포자의 찍기 패턴 
    pattern1 = [1, 2, 3, 4, 5]  
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]  
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  
    
    scores = [0, 0, 0]  
    patterns = [pattern1, pattern2, pattern3]
    
    # 모든 문제에 대해 각 수포자의 답과 정답을 비교
    for i in range(len(answers)):
        correct_answer = answers[i]
        
        # 각 수포자(0, 1, 2번 인덱스)에 대해 확인
        for person in range(3):
            current_pattern = patterns[person]
            
            # 패턴이 반복되므로 % 사용
            person_answer = current_pattern[i % len(current_pattern)]
            
            if person_answer == correct_answer:
                scores[person] += 1 
            else:
                scores[person] += 0
    
    max_score = 0
    for score in scores:
        if score > max_score:
            max_score = score
    
    result = []
    for i in range(3):
        if scores[i] == max_score:
            result.append(i + 1) 
            
    return result