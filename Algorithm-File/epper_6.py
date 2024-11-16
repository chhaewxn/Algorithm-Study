def solution(n):
    # 결과를 저장할 리스트
    answer = [n]  # 초기 값 n을 리스트에 포함
    
    # 값이 1이 될 때까지 반복
    while n != 1:
        if n % 2 == 0:  # n이 짝수인 경우
            n = n // 2
        else:  # n이 홀수인 경우
            n = 3 * n + 1
        
        # 계산된 값을 결과 리스트에 추가
        answer.append(n)
    
    return answer

# 테스트
print(solution(10))  # 출력: [10, 5, 16, 8, 4, 2, 1]
print(solution(6))   # 출력: [6, 3, 10, 5, 16, 8, 4, 2, 1]
