def solution(N, road, K):

    INF = float('inf')
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    
    # 자기 자신으로 거리 0
    for i in range(1, N + 1):
        dist[i][i] = 0
    
    # 도로 정보를 거리 행렬에 추가
    for a, b, c in road:
        # 같은 두 마을을 연결하는 도로가 여러 개 있을 수 있으므로 최솟값 사용
        dist[a][b] = min(dist[a][b], c)
        dist[b][a] = min(dist[b][a], c)
    
    for k in range(1, N + 1):  # 경유지
        for i in range(1, N + 1):  # 출발지
            for j in range(1, N + 1):  # 도착지
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    count = 0
    for i in range(1, N + 1):
        if dist[1][i] <= K:
            count += 1
    
    return count