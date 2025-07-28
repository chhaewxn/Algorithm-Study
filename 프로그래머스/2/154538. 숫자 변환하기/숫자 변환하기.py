from collections import deque

def solution(x, y, n):
    visited = set()
    queue = deque()
    queue.append((x, 0))  # (현재 숫자, 연산 횟수)

    while queue:
        current, count = queue.popleft()
        if current == y:
            return count
        for next_num in (current + n, current * 2, current * 3):
            if next_num <= y and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, count + 1))
    
    return -1  # y에 도달할 수 없는 경우
