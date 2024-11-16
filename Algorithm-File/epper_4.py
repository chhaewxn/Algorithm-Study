def solution(ingredients, cost):
    total_cost = sum(ingredients)
    profit = cost - total_cost
    return profit

# 예제 테스트
print(solution([10, 10, 10], 90))  # 출력: 60
print(solution([100, 100], 1000))  # 출력: 800