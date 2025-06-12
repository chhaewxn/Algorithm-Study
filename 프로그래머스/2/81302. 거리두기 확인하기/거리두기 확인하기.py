from collections import deque

def solution(places):
    answer = []
    
    # 방향 벡터 (상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 각 대기실에 대해 검사하는 함수
    def is_safe(place):
        # 5x5 대기실 좌표 순회
        for i in range(5):
            for j in range(5):
                # 응시자(P)를 찾으면 BFS 실행
                if place[i][j] == 'P':
                    if not bfs(i, j, place):
                        return 0  # 거리두기 실패 시 0 리턴
        return 1  # 모두 거리두기 성공 시 1 리턴

    # BFS로 거리두기 검사
    def bfs(x, y, place):
        queue = deque()
        queue.append((x, y, 0))  # 좌표와 현재 거리 저장
        visited = [[False] * 5 for _ in range(5)]
        visited[x][y] = True
        
        while queue:
            cx, cy, dist = queue.popleft()
            
            # 현재 위치에서 상하좌우 탐색
            for dir in range(4):
                nx = cx + dx[dir]
                ny = cy + dy[dir]
                ndist = dist + 1
                
                # 범위 벗어나면 무시
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue
                # 이미 방문했으면 무시
                if visited[nx][ny]:
                    continue
                # 파티션이면 진행 안 함
                if place[nx][ny] == 'X':
                    continue
                # 맨해튼 거리가 2 이하일 때만 확인
                if ndist <= 2:
                    # 응시자 발견하면 거리두기 실패
                    if place[nx][ny] == 'P':
                        return False
                    # 빈 테이블(O)이면 계속 탐색
                    if place[nx][ny] == 'O':
                        queue.append((nx, ny, ndist))
                        visited[nx][ny] = True
        return True 
    
    for place in places:
        answer.append(is_safe(place))
    
    return answer
