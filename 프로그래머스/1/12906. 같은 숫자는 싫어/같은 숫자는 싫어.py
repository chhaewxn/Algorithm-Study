def solution(arr):
    answer = []
    
    # 배열이 비어있으면 빈 배열 반환
    if not arr:
        return answer
    
    answer.append(arr[0])
    for i in range(1, len(arr)):
        # 현재 원소가 이전에 추가된 원소와 다른 경우에만 추가
        if arr[i] != answer[-1]:
            answer.append(arr[i])
    
    return answer