def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery_stack = []
    pickup_stack = []

    for i in range(n):
        if deliveries[i] != 0:
            delivery_stack.append((i + 1, deliveries[i]))  # (집 위치, 남은 택배 개수)
        if pickups[i] != 0:
            pickup_stack.append((i + 1, pickups[i]))

    # 스택의 맨 위가 항상 가장 먼 위치가 됨
    while delivery_stack or pickup_stack:
        # 가장 먼 곳 거리 구하기
        farthest = 0
        if delivery_stack:
            farthest = max(farthest, delivery_stack[-1][0])
        if pickup_stack:
            farthest = max(farthest, pickup_stack[-1][0])

        answer += farthest * 2

        # 배달 처리
        remain = cap
        while delivery_stack and remain > 0:
            house, count = delivery_stack.pop()
            if count <= remain:
                remain -= count
            else:
                delivery_stack.append((house, count - remain))
                remain = 0

        # 수거 처리
        remain = cap
        while pickup_stack and remain > 0:
            house, count = pickup_stack.pop()
            if count <= remain:
                remain -= count
            else:
                pickup_stack.append((house, count - remain))
                remain = 0

    return answer
