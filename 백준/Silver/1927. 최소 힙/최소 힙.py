import heapq
import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 최소 힙을 저장할 리스트
heap = []

# 연산의 개수를 입력받음
N = int(input())

# 연산을 N번 반복
for _ in range(N):
    # 연산 종류와 값을 입력받음
    op = int(input())

    # 연산이 0인 경우
    if op == 0:
        # 힙이 비어있다면 0 출력
        if not heap:
            print(0)
        else:
            # 힙에서 가장 작은 값을 출력하고 제거
            print(heapq.heappop(heap))
    # 연산이 0이 아닌 경우 (정수 x를 추가하는 연산)
    else:
        # 힙에 정수 x를 추가
        heapq.heappush(heap, op)