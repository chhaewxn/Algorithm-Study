from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    # 다리 위에 있는 트럭을 저장하는 큐 
    bridge = deque()
    
    # 다리 위 트럭의 총 무게
    current_weight = 0
    waiting_trucks = deque(truck_weights)
    
    # 모든 트럭이 다리를 건널 때까지 반복
    while bridge or waiting_trucks:
        time += 1
        
        # 다리를 다 건너간 트럭이 있는지 확인
        if bridge and time - bridge[0][1] == bridge_length:
            truck_weight, _ = bridge.popleft()
            current_weight -= truck_weight
        
        # 대기 중인 트럭이 다리에 진입할 수 있는지 확인
        if waiting_trucks and current_weight + waiting_trucks[0] <= weight and len(bridge) < bridge_length:
            truck_weight = waiting_trucks.popleft()
            bridge.append((truck_weight, time))
            current_weight += truck_weight
    
    return time