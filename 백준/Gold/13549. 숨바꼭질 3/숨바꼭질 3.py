import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
max_size = 100001
visited = [-1] * max_size  # 방문 여부 및 시간을 기록하는 리스트 (-1로 초기화)

def bfs():
    queue = deque([N])
    visited[N] = 0  # 시작 위치의 방문 시간은 0
    while queue:
        current = queue.popleft()
        if current == K:
            return visited[current]
        for next_step in (current * 2, current - 1, current + 1):
            if 0 <= next_step < max_size and visited[next_step] == -1:
                if next_step == current * 2:
                    visited[next_step] = visited[current]
                    queue.appendleft(next_step)  # 우선순위 큐 사용
                else:
                    visited[next_step] = visited[current] + 1
                    queue.append(next_step)

print(bfs())
