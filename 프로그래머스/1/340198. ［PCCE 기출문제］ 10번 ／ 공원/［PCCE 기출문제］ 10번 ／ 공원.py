def solution(mats, park):
    mats.sort(reverse=True)  # 큰 돗자리부터 시도
    rows, cols = len(park), len(park[0])

    # 돗자리 크기 하나씩 시도
    for size in mats:
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                can_place = True
                for di in range(size):
                    for dj in range(size):
                        if park[i + di][j + dj] != "-1":
                            can_place = False
                            break
                    if not can_place:
                        break
                if can_place:
                    return size  # 가장 큰 돗자리 중 하나라도 놓을 수 있으면 반환
    return -1
