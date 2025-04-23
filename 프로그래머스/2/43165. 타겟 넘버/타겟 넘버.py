def solution(numbers, target):
    def dfs(index, current_sum): # DFS 구현으로 모든 경우의 수를 탐색
        if index == len(numbers): # 모든 숫자를 사용했을 때
            # 현재 합계가 타겟과 같으면 1, 아니면 0 반환
            return 1 if current_sum == target else 0
        
        # 현재 숫자를 더하는 경우 + 빼는 경우의 합산
        count = dfs(index + 1, current_sum + numbers[index])
        count += dfs(index + 1, current_sum - numbers[index])
        
        return count
    
    # 0번 인덱스부터 시작, 초기 합계는 0
    return dfs(0, 0)
