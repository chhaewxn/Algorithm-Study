import heapq  

def solution(scoville, K):
    heapq.heapify(scoville)
    mix_count = 0  # 섞은 횟수
    
    # 가장 낮은 스코빌 지수가 K보다 작은 동안 반복
    while scoville[0] < K:
        # 더 이상 섞을 음식이 없으면 목표 달성 불가
        if len(scoville) < 2:
            return -1
        
        # 가장 맵지 않은 음식과 두 번째로 맵지 않은 음식 추출
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        # 새로운 음식 생성: 가장 맵지 않은 음식 + (두 번째로 맵지 않은 음식 * 2)
        new_food = first + (second * 2)
        
        # 새로운 음식을 힙에 추가
        heapq.heappush(scoville, new_food)
        
        # 섞은 횟수 증가
        mix_count += 1
    
    return mix_count