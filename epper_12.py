def solution(command):
    # 로봇의 현재 위치와 방향
    x, y = 0, 0          # 시작 위치는 (0, 0)
    direction = 0        # 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
    
    # 각 방향에 따른 이동 벡터 (북, 동, 남, 서)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 각 명령어 처리
    for cmd in command:
        if cmd == 'R':
            # 오른쪽으로 90도 회전
            direction = (direction + 1) % 4
        elif cmd == 'L':
            # 왼쪽으로 90도 회전
            direction = (direction - 1) % 4
        elif cmd == 'G':
            # 현재 방향으로 한 칸 전진
            x += dx[direction]
            y += dy[direction]
        elif cmd == 'B':
            # 현재 방향의 반대 방향으로 한 칸 후진
            x -= dx[direction]
            y -= dy[direction]
    
    return [x, y]