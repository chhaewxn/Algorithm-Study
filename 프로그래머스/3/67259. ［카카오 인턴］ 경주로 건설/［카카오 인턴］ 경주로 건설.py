from collections import deque

def solution(board):
    n = len(board)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  
    visited = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    
    queue = deque()

    for i, (dx, dy) in enumerate(directions):
        nx, ny = dx, dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            visited[nx][ny][i] = 100
            queue.append((nx, ny, i, 100))

    while queue:
        x, y, dir_idx, cost = queue.popleft()
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                new_cost = cost + 100 if dir_idx == i else cost + 600  # 직선이나 코너
                if visited[nx][ny][i] > new_cost:
                    visited[nx][ny][i] = new_cost
                    queue.append((nx, ny, i, new_cost))
                    
    return min(visited[n-1][n-1])
