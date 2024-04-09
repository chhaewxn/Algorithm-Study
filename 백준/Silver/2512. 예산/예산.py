def calculate_budget(budgets, cap):
    total = 0
    for budget in budgets:
        total += min(budget, cap)
    return total

def binary_search(budgets, target):
    left = 0
    right = max(budgets)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total = calculate_budget(budgets, mid)

        if total <= target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

def main():
    n = int(input())  # 지방의 수
    budgets = list(map(int, input().split()))  # 각 지방의 예산
    total_budget = int(input())  # 총 예산

    budgets.sort()  # 이진 탐색을 위해 예산 정렬

    answer = binary_search(budgets, total_budget)
    print(answer)

if __name__ == "__main__":
    main()
